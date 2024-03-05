from django.urls import path
from . import views


app_name = 'inetpower'

urlpatterns = [
    path('', views.index, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]