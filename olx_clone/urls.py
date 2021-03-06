from . import views
from django.urls import path

app_name = 'olx_clone'

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<slug:product_slug>', views.productDetail, name="product_detail"),
    path('category', views.category, name="category"),
    path('item/<str:category>', views.allCategory, name="item"),
]