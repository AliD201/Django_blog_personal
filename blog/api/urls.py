"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [

    # path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.post_detail, name='blog-detail-api'),
    path('post/new', views.post_create, name='blog-new-api'),
    path('post/<int:id>/update', views.post_update, name='post-update-api'),
    path('post/<int:id>/delete', views.post_delete, name='post-delete-api'),
    path('posts/', views.post_list_view.as_view(), name='posts-list-api'),



]
