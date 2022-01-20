from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'reg_date', 'market', 'name', 'display_name', 'price', 'sale_price', 'cate_item', 'hit_count', 'review_count', 'review_point']
