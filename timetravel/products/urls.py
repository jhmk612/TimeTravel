from django.conf.urls import url
from . import views

app_name='products'

urlpatterns=[
    url('^', views.intro, name='intro'),


]