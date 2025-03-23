from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *


import json

@csrf_exempt  # Use only if CSRF is an issue
def add_lab_tests(request):

    if request.method == "POST":
        
        data = json.loads(request.body)  # Parse JSON data
        test_ids = data.get('test_ids', [])
        test_prices = data.get('test_prices', [])
        lab_id = data.get('lab_id')


        if not lab_id or not test_ids or not test_prices or len(test_ids) != len(test_prices):
            return JsonResponse({"error": "Invalid data"}, status=400)

        try:
            lab_instance = lab.objects.get(id=lab_id)  # Ensure lab exists
        except lab.DoesNotExist:
            return JsonResponse({"error": "Lab not found"}, status=404)

        lab_tests = []
        for test_id, price in zip(test_ids, test_prices):
            try:
                test_instance = test.objects.get(id=test_id)  # Ensure test exists
                lab_tests.append(lab_test(lab=lab_instance, test=test_instance, b2b_price=price, processing_time=24))
            except test.DoesNotExist:
                continue  # Skip invalid test IDs

        if lab_tests:
            lab_test.objects.bulk_create(lab_tests)  # Insert all at once
            return JsonResponse({"message": "Lab tests added successfully"}, status=201)
        else:
            return JsonResponse({"error": "No valid tests to add"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

from .serializers import LabTestSerializer

def get_lab_tests(request):

    lab_id = request.GET.get('lab_id')

    if not lab_id:
        return JsonResponse({"error": "Lab ID is required"}, status=400)

    lab_tests = lab_test.objects.filter(lab__id=lab_id)
    
    if not lab_tests.exists():
        return JsonResponse({"message": "No tests found for this lab"}, status=404)

    serialized_data = LabTestSerializer(lab_tests, many=True).data
    
    return JsonResponse({"data": serialized_data}, status=200, safe=False)




from rest_framework import generics, permissions
from .models import labbotomist_details
from .serializers import LabbotomistDetailsSerializer

class CreateLabbotomistView(generics.CreateAPIView):
    queryset = labbotomist_details.objects.all()
    serializer_class = LabbotomistDetailsSerializer
    # permission_classes = [permissions.IsAdminUser]  # Only admin can create

class UpdateLabbotomistView(generics.UpdateAPIView):
    queryset = labbotomist_details.objects.all()
    serializer_class = LabbotomistDetailsSerializer
    # permission_classes = [permissions.IsAdminUser]


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import labbotomist_details, User
from .forms import labbotomist_details_Form  # Create a form for handling labbotomist data

def add_labbotomist(request):
    
    if request.method == "POST":
        form = labbotomist_details_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_labbotomists')  # Redirect after successful add
        else:
            print(form.errors)

    else:
        form = labbotomist_details_Form()

    return render(request, "lab/add_labbotomist.html", {"form": form})

def update_labbotomist(request, labbotomist_id):
    lab = get_object_or_404(labbotomist_details, pk=labbotomist_id)
    initial_data = {'username': lab.user.username}

    form = labbotomist_details_Form(request.POST or None, instance=lab, initial=initial_data)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_labbotomists')

    return render(request, 'lab/add_labbotomist.html', {'form': form})



def list_labbotomists(request):
    data = labbotomist_details.objects.all()
    return render(request, 'lab/list_labbotomists.html', {'data': data})

def delete_labbotomist(request, labbotomist_id):
    labbotomist = get_object_or_404(labbotomist_details, id=labbotomist_id)
    labbotomist.user.delete()  # This also deletes the labbotomist due to the OneToOne relationship
    return redirect('list_labbotomists')




def get_labbotomist(request):

    data = list(labbotomist_details.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})




from rest_framework.views import APIView
from order.models import *
from order.serializers import *
from rest_framework import status



# class get_order(APIView):

#     def get(self, request, *args, **kwargs):
#         user_id = request.GET.get("user")  # Get user ID from query params
#         order_type = request.GET.get("type")  # Get order type from query params

#         orders = order.objects.all()

#         if user_id:
#             orders = orders.filter(user_id=user_id)

#         if order_type:
#             orders = orders.filter(type=order_type)

#         serializer = order_serializer(orders, many=True)
#         return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *


import json

# @csrf_exempt  # Use only if CSRF is an issue
# def update_order(request, order_id):

#     if request.method == 'POST':

#         try:
#             order_instance = order.objects.get(id=order_id)

#             data = json.loads(request.body)  # Read request body properly
#             order_instance.status = data.get("status", order_instance.status)
#             order_instance.save()

#             return JsonResponse({
#                 "success": True,
#                 "message": "Order status updated!",
#                 "data": {
#                     "order_id": order_instance.id,
#                     "status": order_instance.status
#                 }
#             }, status=200)

#         except order.DoesNotExist:
#             return JsonResponse({"success": False, "message": "Order not found", "data": {}}, status=404)

#         except json.JSONDecodeError:
#             return JsonResponse({"success": False, "message": "Invalid JSON", "data": {}}, status=400)