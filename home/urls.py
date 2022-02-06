from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('other/', other, name='otherpage'),
]
