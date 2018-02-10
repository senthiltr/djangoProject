from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^content/', views.content, name='content'),
]