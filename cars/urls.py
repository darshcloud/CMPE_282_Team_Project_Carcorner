from django.urls import path
from . import views


urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
     path('generate_description/', views.generate_description, name='generate_description'),
]