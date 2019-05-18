from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name='accounts'

urlpatterns=[
    url('^login/$', LoginView.as_view(), name='login'),
    url('^signup/$', views.signup, name='signup'),
    url('^logout/$', LogoutView.as_view(), {'next_page':'home'}, name='logout'),



]