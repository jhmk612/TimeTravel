from django.conf.urls import url
from . import views

app_name='products'

urlpatterns=[
    url('^', views.intro.as_view(), name='intro'),


]