from django.urls import path 
from . import views


urlpatterns = [
path('' ,views.home),
path('notifications/', views.notifications),
path('allnudges/', views.allnudges),
]
