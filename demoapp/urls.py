from django.conf.urls import url
from . import views
#创建子路由

urlpatterns = [
    url(r'^index/$', views.index),
]
