from django.shortcuts import render

# Create your views here.



from .models import *
from masters.models import *


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

class AddToCartView(APIView):


    def post(self, request):
        try:
            # Fetch user instance (use request.user if authenticated)
            user_instance = User.objects.get(id=1)  

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

    def get(self, request):

        cart_items = cart.objects.filter(user__id=1)
        
        medicine_items = []
        test_items = []

        medicine_items = [cartserializer(item).data for item in cart_items if item.type == "medicine"]
        test_items = [cartserializer(item).data for item in cart_items if item.type == "test"]

        return Response({'medicines': medicine_items, 'tests': test_items}, status=200)
