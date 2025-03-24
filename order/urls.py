from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # customer api

    path('apply_coupon/', apply_coupon, name='apply_coupon'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('get_cart_items', get_cart_items.as_view(), name='get_cart_items'),
   
    path('add-order/', add_order.as_view(), name='add_order'),
    path('get-orders/', get_order.as_view(), name='get_order'),
    path('update-orders/<order_id>', update_order, name='update_order'), # for admin
    path('list-orders/<order_type>', list_order, name='list_order'),


    #pharmacy api
    path('orders-recieved-to-hub/', order_recieved_to_hub.as_view(), name='order_recieved_to_hub'),
    path('show-orders-from-pharmacy/<order_type>', show_orders_from_pharmacy.as_view(), name='show_orders_from_pharmacy'),
    path('get-orders-from-pharmacy/', get_orders_from_pharmacy.as_view(), name='get_orders_from_pharmacy'),
    path('your-orders-labbotomist/<order_type>', your_order_labbotomist, name='list_order_labbotomist'),



] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)