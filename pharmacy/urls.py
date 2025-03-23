from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [



    path('add-pharmacy/', add_pharmacy, name='add_pharmacy'),
    path('update-pharmacy/<int:pharmacy_id>/', update_pharmacy, name='update_pharmacy'),
    path('list-pharmacy/', list_pharmacy, name='list_pharmacy'),
    path('delete-pharmacy/<int:pharmacy_id>/', delete_pharmacy, name='delete_pharmacy'),
    path('get-pharmacy/', get_pharmacy, name='get_pharmacy'),

    path('login-pharmacy/', pharmacy_login.as_view(), name='login_pharmacy'),
    path('signup-pharmacy/', pharmacy_signup.as_view(), name='signup_pharmacy'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)