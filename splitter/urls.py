from django.urls import path
from splitter import views

urlpatterns = [
    path('', views.HomePage, name="home"),
]