from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workshops, name='workshops'),
    path('<str:slug>', views.GoToWorkshop, name='WorkshopMain'),
    # path('done', views.submit, name="Submit")
]
