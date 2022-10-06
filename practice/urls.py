from django.urls import path, include
from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.CameraView.as_view(), name='practice'),
    path('camera', views.camera, name='camera'),
]