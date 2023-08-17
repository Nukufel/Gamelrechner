from django.urls import path
from . import views

urlpatterns = [
    path('<str:gender>/', views.form, name='form'),
    path('<str:gender>/result/', views.result, name='result'),
    path('', views.start, name='start')

]