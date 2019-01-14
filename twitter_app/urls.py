from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseindexview, name="home"),
]
