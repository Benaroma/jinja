from django.urls import path
from JinjaApp import views

urlpatterns = [
    path('home/', views.home, name='my_home'),
    path('contact/', views.contact, name='my_contact'),
    path('about/', views.about, name='my_about'),
    path('gallery/', views.gallery, name='my_gallery')
]
