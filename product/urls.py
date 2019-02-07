from django.urls import path

from .views import ProductListView, ProductDetailView

app_name = 'product'
urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product_detail'),
]