from django.urls import path
from django.conf.urls import url
from broadcast import views

urlpatterns = [
    url(r'broadcast$', views.broadcast_sms, name="default"),
]
