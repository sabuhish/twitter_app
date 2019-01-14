from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseindexview, name="home"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('timeline/slug/', views.timeline_view, name="timeline"),
]
