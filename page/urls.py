from django.urls import path
from .views import *

app_name = 'page'
urlpatterns = [
    path('', IndexView.as_view(), name='index')
]