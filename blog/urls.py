"""
URL configuration for project_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('',login_required(views.homeView.as_view()),name='home'),
    path('profile/',login_required(views.profileView.as_view()),name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', views.logoutView.as_view(),name='logout'),
    path('register/',views.registerView.as_view(),name='register'),
    path('profile/update',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('',login_required(homeListView.as_view()),name='home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='delete'),
    path('new/post',NewPost.as_view(),name='newpost')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
