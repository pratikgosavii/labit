from django.shortcuts import render

# Create your views here.


from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





@login_required(login_url='login')
def add_doctor(request):

    if request.method == 'POST':

        forms = doctor_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_doctor')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_doctor.html', context)
    
    else:

        forms = doctor_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_doctor.html', context)


from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login')
@csrf_exempt 
def add_doctor_json(request):

    if request.method == 'POST':
        form = doctor_Form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Doctor added successfully'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

        

@login_required(login_url='login')
def update_doctor(request, doctor_id):

    if request.method == 'POST':

        instance = doctor.objects.get(id=doctor_id)

        print('-------------------')
        print('-------------------')
        print('-------------------')
        print(instance.user)

        updated_request = request.POST.copy()
        updated_request.update({'user': instance.user})

        forms = doctor_Form(updated_request, request.FILES, instance=instance)

        print(forms.instance.user)

        if forms.is_valid():
            forms.save()
            return redirect('list_doctor')
        else:
            print(forms.errors)
    
    else:

        instance = doctor.objects.get(id=doctor_id)
        forms = doctor_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_doctor.html', context)

        

@login_required(login_url='login')
def delete_doctor(request, doctor_id):

    doctor.objects.get(id=doctor_id).delete()

    return HttpResponseRedirect(reverse('list_doctor'))


@login_required(login_url='login')
def list_doctor(request):

    data = doctor.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_doctor.html', context)


from django.http import JsonResponse

def get_doctor(request):

    data = list(doctor.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})



@login_required(login_url='login')
def list_doctor(request):

    data = doctor.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_doctor.html', context)



@login_required(login_url='login')
def add_test(request):

    if request.method == 'POST':

        forms = test_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_test')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_test.html', context)
    
    else:

        forms = test_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_test.html', context)

        

@login_required(login_url='login')
def update_test(request, test_id):

    if request.method == 'POST':

        instance = test.objects.get(id=test_id)

        forms = test_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_test')
        else:
            print(forms.errors)
    
    else:

        instance = test.objects.get(id=test_id)
        forms = test_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_test.html', context)

        

@login_required(login_url='login')
def delete_test(request, test_id):

    test.objects.get(id=test_id).delete()

    return HttpResponseRedirect(reverse('list_test'))


@login_required(login_url='login')
def list_test(request):

    data = test.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_test.html', context)


from django.http import JsonResponse

def get_test(request):

    data = list(test.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})


@login_required(login_url='login')
def add_lab(request):

    if request.method == 'POST':

        forms = lab_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_lab')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_lab.html', context)
    
    else:

        forms = lab_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_lab.html', context)

        

@login_required(login_url='login')
def update_lab(request, lab_id):

    if request.method == 'POST':

        instance = lab.objects.get(id=lab_id)

        forms = lab_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_lab')
        else:

            context = {
                'form': forms
            }

            return render(request, 'add_lab.html', context)
    
    else:

        instance = lab.objects.get(id=lab_id)
        forms = lab_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_lab.html', context)

        

@login_required(login_url='login')
def delete_lab(request, lab_id):

    lab.objects.get(id=lab_id).delete()

    return HttpResponseRedirect(reverse('list_lab'))


@login_required(login_url='login')
def list_lab(request):

    data = lab.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_lab.html', context)


from django.http import JsonResponse

def get_lab(request):

    data = list(lab.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})


@login_required(login_url='login')
def add_coupon(request):

    if request.method == 'POST':

        forms = coupon_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_coupon')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_coupon.html', context)
    
    else:

        forms = coupon_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_coupon.html', context)

        

@login_required(login_url='login')
def update_coupon(request, coupon_id):

    if request.method == 'POST':

        instance = coupon.objects.get(id=coupon_id)

        forms = coupon_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_coupon')
        else:
            print(forms.errors)

            context = {
                'form': forms
            }

            return render(request, 'add_coupon.html', context)
    
    else:

        instance = coupon.objects.get(id=coupon_id)
        forms = coupon_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_coupon.html', context)

        

@login_required(login_url='login')
def delete_coupon(request, coupon_id):

    coupon.objects.get(id=coupon_id).delete()

    return HttpResponseRedirect(reverse('list_coupon'))


@login_required(login_url='login')
def list_coupon(request):

    data = coupon.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_coupon.html', context)


from django.http import JsonResponse

def get_coupon(request):

    data = list(coupon.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})


@login_required(login_url='login')
def add_medicine_category(request):

    if request.method == 'POST':

        forms = medicine_category_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_medicine_category')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_medicine_category.html', context)
    
    else:

        forms = medicine_category_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_medicine_category.html', context)

        

@login_required(login_url='login')
def update_medicine_category(request, medicine_category_id):

    if request.method == 'POST':

        instance = medicine_category.objects.get(id=medicine_category_id)

        forms = medicine_category_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_medicine_category')
        else:
            print(forms.errors)

            context = {
                'form': forms
            }

            return render(request, 'add_medicine_category.html', context)
    
    else:

        instance = medicine_category.objects.get(id=medicine_category_id)
        forms = medicine_category_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_medicine_category.html', context)

        

@login_required(login_url='login')
def delete_medicine_category(request, medicine_category_id):

    medicine_category.objects.get(id=medicine_category_id).delete()

    return HttpResponseRedirect(reverse('list_medicine_category'))


@login_required(login_url='login')
def list_medicine_category(request):

    data = medicine_category.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_medicine_category.html', context)


from django.http import JsonResponse

def get_medicine_category(request):

    data = list(medicine_category.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})


@login_required(login_url='login')
def add_medicine(request):

    if request.method == 'POST':

        forms = medicine_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_medicine')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }
            return render(request, 'add_medicine.html', context)
    
    else:

        forms = medicine_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_medicine.html', context)

        

@login_required(login_url='login')
def update_medicine(request, medicine_id):

    if request.method == 'POST':

        instance = medicine.objects.get(id=medicine_id)

        forms = medicine_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_medicine')
        else:

            context = {
                'form': forms
            }

            return render(request, 'add_medicine.html', context)
    
    else:

        instance = medicine.objects.get(id=medicine_id)
        forms = medicine_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_medicine.html', context)

        

@login_required(login_url='login')
def delete_medicine(request, medicine_id):

    medicine.objects.get(id=medicine_id).delete()

    return HttpResponseRedirect(reverse('list_medicine'))


@login_required(login_url='login')
def list_medicine(request):

    data = medicine.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_medicine.html', context)


from django.http import JsonResponse

def get_medicine(request):

    data = list(medicine.objects.values())  # ✅ Converts QuerySet to a list of dictionaries
    return JsonResponse({'data': data})




from .models import *


def add_testimonials(request):
    
    if request.method == "POST":

        description = request.POST.get('description')
        name = request.POST.get('name')

        print(description)
        print(name)

        instance = testimonials.objects.create(description = description, name = name)
        instance.save()

        return redirect('list_testimonials')
    
    else:

        # create first row using admin then editing only

        

        return render(request, 'add_testimonials.html', { 'form' : testimonials_Form()})

def update_testimonials(request, testimonials_id):
    
    instance = testimonials.objects.get(id = testimonials_id)

    if request.method == "POST":

        description = request.POST.get('description')
        name = request.POST.get('name')

        print(description)
        print(name)

        instance.description = description
        instance.name = name
        instance.save()

        return redirect('list_testimonials')
    
    else:

        # create first row using admin then editing only

        

        return render(request, 'add_testimonials.html', {'data' : instance})


def list_testimonials(request):

    data = testimonials.objects.all()

    return render(request, 'list_testimonials.html', {'data' : data})


def delete_testimonials(request, testimonials_id):

    data = testimonials.objects.get(id = testimonials_id).delete()

    return redirect('list_testimonials')


from django.views import View


def get_testimonials(request):
  
    data = testimonials.objects.all()  # Assuming Testimonials is the model name

    if not data.exists():
        return JsonResponse({"error": "No data found"}, status=404)

    response_data = []
    for testimonial in data:
        temp = {
            "id": testimonial.id,
            "name": testimonial.name,
            "description": testimonial.description,
        }
        response_data.append(temp)

    return JsonResponse({"data": response_data}, status=200)

def add_home_banner(request):
    
    if request.method == "POST":

        forms = home_banner_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_home_banner')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }

            return render(request, 'add_home_banner.html', context)
    
    else:

        # create first row using admin then editing only

        

        return render(request, 'add_home_banner.html', { 'form' : home_banner_Form()})

def update_home_banner(request, home_banner_id):
    
    instance = home_banner.objects.get(id = home_banner_id)

    if request.method == "POST":


        instance = home_banner.objects.get(id=home_banner_id)

        forms = home_banner_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_home_banner')
        else:
            print(forms.errors)
            context = {
                'form': forms
            }

            return render(request, 'add_home_banner.html', context)

    
    else:

        # create first row using admin then editing only

        

        return render(request, 'add_home_banner.html', {'data' : instance})


def list_home_banner(request):

    data = home_banner.objects.all()

    return render(request, 'list_home_banner.html', {'data' : data})


def delete_home_banner(request, home_banner_id):

    data = home_banner.objects.get(id = home_banner_id).delete()

    return redirect('list_home_banner')


from django.views import View
from .serializer import *

def get_home_banner(request):
  
    data = home_banner.objects.all()  # Assuming home_banner is the model name


    serialized_data = HomeBannerSerializer(data, many=True).data  

    return JsonResponse({"data": serialized_data}, status=200, safe=False)  
