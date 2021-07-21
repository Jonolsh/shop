from django.conf.urls import url
from django.urls import path
from . import views


app_name= 'coupons'

urlpatterns = [
	# url(r'^apply/$', views.coupon_apply, name='apply'),
	path('apply/', views.coupon_apply, name='apply'),
]