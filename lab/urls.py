from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('add-lab-tests/', add_lab_tests, name='add_lab_tests'),
    path('get-lab-tests/', get_lab_tests, name='get_lab_tests'),


    path('create-labbotomist/', CreateLabbotomistView.as_view(), name='create_labbotomist'),
    path('update-labbotomist-json/<int:pk>/', UpdateLabbotomistView.as_view(), name='update_labbotomist'),


    path('add-labbotomist/', add_labbotomist, name='add_labbotomist'),
    path('update-labbotomist/<int:labbotomist_id>/', update_labbotomist, name='update_labbotomist'),
    path('list-labbotomists/', list_labbotomists, name='list_labbotomists'),
    path('delete-labbotomist/<int:labbotomist_id>/', delete_labbotomist, name='delete_labbotomist'),
    path('get-labbotomist/', get_labbotomist, name='get_labbotomist'),

    path('get-orders/', get_order.as_view(), name='get_order'),
    path('update-order/<order_id>', update_order, name='update_orders'),


] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)