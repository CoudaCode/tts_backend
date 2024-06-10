from django.urls import path
from .views import *

urlpatterns = [
    path('text-to-speech/', text_to_speech, name='text_to_speech'),
]