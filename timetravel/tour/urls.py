from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name='tour'

urlpatterns=[
    url('^$', views.tour, name='tour'),


]