from django.urls import path

from .views import login_page, logout_page, user_list

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('user_list/', user_list, name='user_list'),
]
