from turtle import home
from django.urls import path
from app import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('blog_detail/<int:pk>/', views.Blog_Detail, name='blog_detail'),
    path('category/<str:cat>/',views.Category,name='category'),
    path('auth/', views.Auth, name='auth'),
    path('register/', views.Register, name='register'),
    path('login/', views.Calculater, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('add-post/', views.Add_Post, name='add_post'),
    path('delete-post/<int:pk>/', views.Delete_Post, name='delete-post'),
]
