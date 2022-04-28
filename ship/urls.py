from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_ship),
    path('<int:id>', views.ship_details)
]
