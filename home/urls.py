from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('other/', other, name='otherPage'),
    path('about/', about, name='about'),
]
