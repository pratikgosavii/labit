from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import pharmacy, User
from .forms import pharmacy_Form  # Create a form for handling pharmacy data

def add_pharmacy(request):
    
    if request.method == "POST":
        form = pharmacy_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pharmacys')  # Redirect after successful add
        else:
            print(form.errors)

    else:
        form = pharmacy_Form()

    return render(request, "pharmacy/add_pharmacy.html", {"form": form})

def update_pharmacy(request, pharmacy_id):
    lab = get_object_or_404(pharmacy, pk=pharmacy_id)
    initial_data = {'username': lab.user.username}

    form = pharmacy_Form(request.POST or None, instance=lab, initial=initial_data)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_pharmacy')

    return render(request, 'pharmacy/add_pharmacy.html', {'form': form})



def list_pharmacy(request):
    data = pharmacy.objects.all()
    return render(request, 'pharmacy/list_pharmacy.html', {'data': data})

def delete_pharmacy(request, pharmacy_id):
    pharmacy = get_object_or_404(pharmacy, id=pharmacy_id)
    pharmacy.user.delete()  # This also deletes the pharmacy due to the OneToOne relationship
    return redirect('list_pharmacy')




def get_pharmacy(request):

    data = list(pharmacy.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})



