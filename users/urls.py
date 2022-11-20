from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profile_page, name ="users"),
    path('update_profile/', views.update_profile, name = "update_profile"),
]