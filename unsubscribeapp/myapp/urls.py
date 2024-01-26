from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-emails/', views.get_emails, name='get_emails'),
    path('edit-emails/', views.edit_emails, name='edit_emails'),
    path('delete-emails/', views.delete_emails, name='delete_emails'),
    path('download-emails/', views.download_emails, name='download_emails'),
    path('search-emails/', views.search_emails, name='search_emails'),
]
