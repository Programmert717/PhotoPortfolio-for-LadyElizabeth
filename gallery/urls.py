from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from gallery import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload_photo, name='upload'),
    path('delete/<int:photo_id>', views.delete_photo, name='delete_photo'),
]
