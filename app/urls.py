from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage,name="signuppage"),
    path('login/', views.loginpage,name="loginpage"),
    path('home/', views.home,name="homepage"),
    path('add/', views.addpage,name="addpage"),
    path('update/<str:id>', views.updatepage,name="updatepage"),
    path('delete/<str:id>', views.deletepage,name="deletepage"),
    path('logout', views.logoutpage,name="logoutpage"),
]