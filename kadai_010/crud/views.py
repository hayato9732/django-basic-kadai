from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product  # 商品のモデルをインポート

# 商品詳細表示用のビュー
class ProductDetailView(DetailView):
    model = Product  # 商品モデルを指定
    template_name = 'crud/product_detail.html'  # 使用するテンプレート
    context_object_name = 'product'  # テンプレート内で使う変数名