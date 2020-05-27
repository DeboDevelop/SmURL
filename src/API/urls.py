from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('urls/', URLAPIView.as_view()),
    path('urls/<int:pk>/', URLDetail.as_view()),
]
