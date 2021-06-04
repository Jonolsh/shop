from django.conf.urls import url
from . import views
from django.urls import path

app_name= 'shop'

# http://127.0.0.1:8000/shop/

# views.product_list
# http://127.0.0.1:8000/shop/slug/
# http://127.0.0.1:8000/shop/fructs/


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:category_slug>/', views.product_list,
        name='product_list_by_category'),
    # http://127.0.0.1:8000/shop/2/apelsin/
    path('<int:id>/<str:slug>/', views.product_detail,
        name='product_detail'),
    path('main_page/', views.main_page, name='main_page'),
]