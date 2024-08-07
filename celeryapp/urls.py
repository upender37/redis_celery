from django.urls import path
from celeryapp import views

urlpatterns = [
    path('', views.add_view, name='home'),
]