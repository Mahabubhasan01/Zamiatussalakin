
from django.urls import path
from app import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('blogs/', views.Total_Blog_Post, name='blogs'),
    path('P<pk>[0-9a-f-]', views.Blog_Detail, name='blog_detail'),
    path('P<pk>[0-9a-f-]', views.Notice_Details, name='notice_details'),
    path('category/<str:cat>/', views.Category, name='category'),
    path('auth/', views.Auth, name='auth'),
    path('register/', views.Register, name='register'),
    path('login/', views.Calculater, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('add-post/', views.Add_New_Post, name='add_post'),
    path('Notice-notifications/', views.NoticeWithNotifications, name='noti-fic'),
    path('P<pk>[0-9a-f-]/', views.Delete_Post, name='delete-post'),
    path('users', views.Users, name='users'),
    path('dashboard_home', views.Dashboard_Home, name='dashboard_home'),
    path('delete-user/<int:pk>/', views.Delete_User, name='delete-user'),
    path('make-admin/<int:pk>/', views.Super_User, name='make-admin'),
    path('chat/',views.Inbox_chatting,name='chat'),
    path('logout', views.User_logout, name='logout'),
]
