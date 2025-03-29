from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('login-lab/', lab_login.as_view(), name='login_lab'),
    path('signup-lab/', lab_signup.as_view(), name='signup_lab'),

    path('add-lab-tests/', add_lab_tests, name='add_lab_tests'),
    path('get-lab-tests/', get_lab_tests.as_view(), name='get_lab_tests'),

    path('get-vendor-orders', get_vendor_order.as_view(), name='get_vendor_order'),


    path('signup-labbotomist/', CreateLabbotomistView.as_view(), name='signup_labbotomist'),
    path('login-labbotomist/', labbotomist_login.as_view(), name='signup_labbotomist'),
    path('update-labbotomist-json/<int:pk>/', UpdateLabbotomistView.as_view(), name='update_labbotomist'),


    path('add-labbotomist/', add_labbotomist, name='add_labbotomist'),
    path('update-labbotomist/<int:labbotomist_id>/', update_labbotomist, name='update_labbotomist'),
    path('list-labbotomists/', list_labbotomists, name='list_labbotomists'),
    path('delete-labbotomist/<int:labbotomist_id>/', delete_labbotomist, name='delete_labbotomist'),
    path('get-labbotomist/', get_labbotomist, name='get_labbotomist'),



] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)