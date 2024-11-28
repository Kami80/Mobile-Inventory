from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_mobile, name='add_mobile'),
    path('edit/<int:pk>/', views.edit_mobile, name='edit_mobile'),
    path('delete/<int:pk>/', views.delete_mobile, name='delete_mobile'),
    path('add-brand/', views.add_brand, name='add_brand'),  # New path for adding brands
]