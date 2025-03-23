from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_page, name='logout'),
    
    path('user_list/', user_list, name='user_list'),
]
