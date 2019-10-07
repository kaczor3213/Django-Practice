from django.urls import path
from .views import *

urlpatterns = [
    path('', SliderView.as_view()),
]
