from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('add-doctor/', add_doctor, name='add_doctor'),
    path('add-doctor-json/', add_doctor_json, name='add_doctor_json'),
    path('update-doctor/<doctor_id>', update_doctor, name='update_doctor'),
    path('delete-doctor/<doctor_id>', delete_doctor, name='delete_doctor'),
    path('list-doctor/', list_doctor, name='list_doctor'),
    path('get-doctor/', get_doctor, name='get_doctor'),

    path('add-test/', add_test, name='add_test'),
    path('update-test/<test_id>', update_test, name='update_test'),
    path('delete-test/<test_id>', delete_test, name='delete_test'),
    path('list-test/', list_test, name='list_test'),
    path('get-test/', get_test, name='get_test'),

    path('add-lab/', add_lab, name='add_lab'),
    path('update-lab/<lab_id>', update_lab, name='update_lab'),
    path('delete-lab/<lab_id>', delete_lab, name='delete_lab'),
    path('list-lab/', list_lab, name='list_lab'),
    path('get-lab/', get_lab, name='get_lab'),

    path('add-coupon/', add_coupon, name='add_coupon'),
    path('update-coupon/<coupon_id>', update_coupon, name='update_coupon'),
    path('delete-coupon/<coupon_id>', delete_coupon, name='delete_coupon'),
    path('list-coupon/', list_coupon, name='list_coupon'),
    path('get-coupon/', get_coupon, name='get_coupon'),

    path('add-medicine_category/', add_medicine_category, name='add_medicine_category'),
    path('update-medicine_category/<medicine_category_id>', update_medicine_category, name='update_medicine_category'),
    path('delete-medicine_category/<medicine_category_id>', delete_medicine_category, name='delete_medicine_category'),
    path('list-medicine_category/', list_medicine_category, name='list_medicine_category'),
    path('get-medicine_category/', get_medicine_category, name='get_medicine_category'),

    path('add-medicine/', add_medicine, name='add_medicine'),
    path('update-medicine/<medicine_id>', update_medicine, name='update_medicine'),
    path('delete-medicine/<medicine_id>', delete_medicine, name='delete_medicine'),
    path('list-medicine/', list_medicine, name='list_medicine'),
    path('get-medicine/', get_medicine, name='get_medicine'),


    path('add-testimonials/', add_testimonials, name='add_testimonials'),  # create or fetch list of admins
    path('update-testimonials/<testimonials_id>', update_testimonials, name='update_testimonials'),  # create or fetch list of admins
    path('list-testimonials/', list_testimonials, name='list_testimonials'),  # create or fetch list of admins
    path('delete-testimonials/<testimonials_id>', delete_testimonials, name='delete_testimonials'),  # create or fetch list of admins
    path('get-testimonials/', get_testimonials, name='get_testimonials'), 

    path('add-home-banner/', add_home_banner, name='add_home_banner'),  # create or fetch list of admins
    path('update-home-banner/<home_banner_id>', update_home_banner, name='update_home_banner'),  # create or fetch list of admins
    path('list-home-banner/', list_home_banner, name='list_home_banner'),  # create or fetch list of admins
    path('delete-home-banner/<home_banner_id>', delete_home_banner, name='delete_home_banner'),  # create or fetch list of admins
    path('get-home-banner/', get_home_banner, name='get_home_banner'), 





] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)