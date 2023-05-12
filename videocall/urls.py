from django.urls import path

from . import views

urlpatterns = [
    path('', views.vc, name='videocall'),
    path('stream/', views.stream, name='stream')
]