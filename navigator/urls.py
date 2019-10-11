from django.urls import path, include
from .views import ListApps

urlpatterns = [
    path('', ListApps.as_view()),
]