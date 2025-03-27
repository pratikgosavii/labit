from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

# Create your views here.



from .models import *
from masters.models import *

from users.permissions import *




def apply_coupon(cart_total, coupon_code):
    try:
        coupon_instance = coupon.objects.get(code=coupon_code, is_active=True, start_date__lte=now(), end_date__gte=now())
    except coupon.DoesNotExist:
        return {"error": "Invalid or expired coupon"}

    if cart_total < coupon_instance.min_purchase:
        return {"error": f"Minimum purchase required: ₹{coupon_instance.min_purchase}"}

    # Calculate discount
    if coupon_instance.discount_percentage:
        discount = (cart_total * coupon_instance.discount_percentage) / 100
    else:
        discount = coupon_instance.discount_amount

    # Apply max discount limit
    if coupon_instance.max_discount and discount > coupon_instance.max_discount:
        discount = coupon_instance.max_discount

    final_price = cart_total - discount

    return {
        "discount": discount,
        "final_price": final_price,
        "message": f"coupon applied successfully! Discount: ₹{discount}"
    }



from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from .models import cart
from .serializers import cartserializer
from rest_framework.permissions import IsAuthenticated



class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]  

    def post(self, request):
        try:
            # Fetch user instance (use request.user if authenticated)
            user_instance = request.user

            item_type = request.data.get('type')  # Use request.data for JSON support
            object_id = request.data.get('object_id')

            if not object_id or not item_type:
                return Response({"error": "Missing required fields"}, status=400)

            object_id = int(object_id)

            if item_type == "test":
                item = test.objects.filter(id=object_id).first()
                if not item:
                    return Response({"error": "Test not found"}, status=400)

                cart_item, created = cart.objects.get_or_create(
                    user=user_instance, type="test", test=item,
                    defaults={'quantity': 1}
                )

            elif item_type == "medicine":
                item = medicine.objects.filter(id=object_id).first()
                if not item:
                    return Response({"error": "Medicine not found"}, status=400)

                cart_item, created = cart.objects.get_or_create(
                    user=user_instance, type="medicine", medicine=item,
                    defaults={'quantity': 1}
                )

            else:
                return Response({"error": "Invalid type"}, status=400)

            # If item already exists, increment quantity by 1
            if not created:
                cart_item.quantity += 1
                cart_item.save()

            return Response(cartserializer(cart_item).data, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
        



class get_cart_items(APIView):

    permission_classes = [IsCustomer]  

    def get(self, request):

        cart_items = cart.objects.filter(user=request.user)
        
        medicine_items = []
        test_items = []

        medicine_items = [cartserializer(item).data for item in cart_items if item.type == "medicine"]
        test_items = [cartserializer(item).data for item in cart_items if item.type == "test"]

        return Response({'medicines': medicine_items, 'tests': test_items}, status=200)


from .serializers import *
from users.permissions import *

from django.db import transaction 

class add_order(APIView):

    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        cart_ids = request.data.get("cart_ids", [])  # List of cart item IDs
        transaction_id = request.data.get("transaction_id")  # Payment transaction ID
        payment_status = request.data.get("payment_status", "pending")  # Default to "pending"

        if not cart_ids:
            return Response({"error": "Cart IDs are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch cart items belonging to the user
        cart_items = cart.objects.filter(id__in=cart_ids, user=request.user)

        if not cart_items.exists():
            return Response({"error": "No valid cart items found"}, status=status.HTTP_400_BAD_REQUEST)

        # Determine order type (assuming all items in cart belong to the same type)
        order_type = cart_items.first().type  
        total_price = sum(
            (item.test.b2b_price if item.type == "test" else item.medicine.price) * item.quantity
            for item in cart_items
        )

        with transaction.atomic():  # Ensure atomicity (rollback on failure)
            # Create order
            order_instance = order.objects.create(
                user=request.user,
                type=order_type,
                total_price=total_price,
                payment_status=payment_status,
                transaction_id=transaction_id  # Store transaction ID
            )

            # Transfer cart items to order_items
            order_items = [
                order_item(
                    order=order_instance,
                    lab_test=item.test if item.type == "test" else None,
                    medicine=item.medicine if item.type == "medicine" else None,
                    quantity=item.quantity,
                    is_labitnow=item.is_labitnow,
                    price=item.test.b2b_price if item.type == "test" else item.medicine.price
                )
                for item in cart_items
            ]

            order_item.objects.bulk_create(order_items)  # Insert all order items efficiently

            # Optional: Clear processed cart items
            cart_items.delete()

        return Response({
            "message": "Order placed successfully!",
            "order_id": order_instance.id,
            "payment_status": payment_status,
            "transaction_id": transaction_id
        }, status=status.HTTP_201_CREATED)

    

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *

class get_order(APIView):
    
    permission_classes = [IsCustomer]  

    def get(self, request, *args, **kwargs):
        user_instance = request.user
        object_type = request.GET.get("type")  # Get order type from query params

        # Apply filters efficiently
        filters = {"user": user_instance}
        if object_type:
            filters["type"] = object_type

        orders_data = order.objects.filter(**filters)
        serializer = order_serializer(orders_data, many=True, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)



from .forms import *


def update_order(request, order_id):

    if request.method == 'POST':

        instance = order.objects.get(id=order_id)

        forms = order_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_order', order_type = 'test')
        else:

            context = {
                'form': forms
            }

            return render(request, 'order/update_order.html', context)
    
    else:

        instance = order.objects.get(id=order_id)
        forms = order_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'order/update_order.html', context)


def list_order(request, order_type):

    data = order.objects.filter(type = order_type)
    print(data)
    context = {
        'data': data
    }

    
    return render(request, 'order/list_order.html', context)




from django.views.decorators.csrf import csrf_exempt


from django.views import View

from users.permissions import *

class order_recieved_to_hub(APIView):

    permission_classes = [IsPharmacist]  

    def post(self, request, *args, **kwargs):
        pharmacy_id = request.data.get('pharmacy_id')
        order_id = request.data.get('order_id')

        if not pharmacy_id or not order_id:
            return Response({"error": "pharmacy_id and order_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch order object safely
        order_obj = get_object_or_404(order, id=order_id)

        # Update the pharmacy_id
        order_obj.pharmacy_id = pharmacy_id
        order_obj.save()

        return Response({"message": "Success"}, status=status.HTTP_200_OK)

    
class show_orders_from_pharmacy(APIView):
    
    permission_classes = [IsLabbotomist]  

    def get(self, request, order_type, *args, **kwargs):

        data = order.objects.filter(pharmacy__isnull=False, type=order_type)
        serialized_data = order_serializer(data, many=True).data  # Serialize queryset

        return Response({"data": serialized_data}, status=status.HTTP_200_OK)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import hub_to_vendor
from .serializers import HubToVendorSerializer

class get_orders_from_pharmacy_to_vendor(APIView):

    permission_classes = [IsLabbotomist]  

    def post(self, request):
        serializer = HubToVendorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Hub to Vendor entry created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class your_order_labbotomist(APIView):

    permission_classes = [IsLabbotomist]  

    def get(self, request, order_type):

        labbotomist_instance = labbotomist_details.objects.get(user = request.user)

        data = order.objects.filter(type=order_type, labbotomist = labbotomist_instance).values()  # Convert queryset to list of dicts
        data2 = hub_to_vendor.objects.filter(labbotomist = labbotomist_instance).values()  # Convert queryset to list of dicts
        
        return JsonResponse({"orders": list(data), "hub_to_vendor": list(data2)}, safe=False)
