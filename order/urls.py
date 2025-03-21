from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('apply_coupon/', apply_coupon, name='apply_coupon'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('get_cart_items', get_cart_items.as_view(), name='get_cart_items'),
   
    path('add-order/', add_order.as_view(), name='add_order'),
    path('get-orders/', get_order.as_view(), name='get_order'),



] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)