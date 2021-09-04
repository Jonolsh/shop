from django.conf.urls import url
from django.urls import path
from . import views

app_name= 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('api/checkout-session/<id>/', views.create_checkout_session, name='api_checkout_session'),

]