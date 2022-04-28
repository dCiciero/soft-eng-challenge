from django.urls import path
from . import views

urlpatterns = [
    path('', views.mothership),
    path('<int:id>', views.mothership_details)
]
