from django.urls import path
from . import views

urlpatterns = [
        path('', views.quote_of_the_day, name='quote_of_the_day'),
    ]