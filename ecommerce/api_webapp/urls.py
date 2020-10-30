from django.urls import path
from .views import *


urlpatterns =[
    path ('', TestingAPI.as_view(),name ='api_home'),
]