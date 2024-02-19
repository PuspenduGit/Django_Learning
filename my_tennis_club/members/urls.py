from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('add/', views.add, name = 'add'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name = 'testing'),
]