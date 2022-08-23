from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'), 

    path('profile_list_view/', views.profile_list_view, name='profile_list_view'), 
    path('profile_list_view/<id>/', views.profile_detail_view, name='profile_detail_view'), 

    path('register/', views.register, name='register'), 
    path('dashboard/', views.dashboard, name='dashboard'), 

]