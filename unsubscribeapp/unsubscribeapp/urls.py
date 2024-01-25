from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('get-emails/', views.download_emails, name='get_emails'),
    path('edit-emails/', views.edit_emails, name='edit_emails'),
    path('delete-emails/', views.delete_emails, name='delete_emails'),
    path('download-emails/', views.download_emails, name='download_emails'),
]
