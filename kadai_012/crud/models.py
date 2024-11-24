from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # 商品名
    description = models.TextField(blank=True, null=True)  # 商品詳細説明
    category = models.CharField(max_length=255)  # カテゴリ
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # 商品画像

    def __str__(self):
        return self.name