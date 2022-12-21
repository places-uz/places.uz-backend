from rest_framework import serializers
from products.serializers.product import ProductSerializer
from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField('get_products_count')

    class Meta:
        model = Category
        fields = ['name', 'is_visible', 'products', 'products_count']

    def get_products_count(self, obj):
        return len(ProductSerializer(obj.products, many=True).data)
