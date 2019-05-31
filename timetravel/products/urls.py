from django.conf.urls import url
from . import views

app_name='products'

urlpatterns=[
    url(r'^$', views.intro.as_view(), name='intro'),
    url(r'^1/$',views.gwanghwamun.as_view(), name='gwanghwamun'),
    url(r'^2/$',views.jamsil.as_view(), name='jamsil'),
    url(r'^3/$',views.yeouido.as_view(), name='yeouido'),

]