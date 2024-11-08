from django.urls import path
from crud.views import ProductDetailView

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]