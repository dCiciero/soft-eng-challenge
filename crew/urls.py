from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_crew),
    path('<int:id>', views.crew_details)
]
