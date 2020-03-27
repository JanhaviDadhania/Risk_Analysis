from django.urls import path
from . import views

urlpatterns = [
    path('', views.transplant, name='transplant'),
    path('death', views.death, name='death')
]
