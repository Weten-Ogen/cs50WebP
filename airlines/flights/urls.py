from django.urls import path
from . import views


# All Urls for flights
urlpatterns = [
  path('',views.index, name='index'),
]