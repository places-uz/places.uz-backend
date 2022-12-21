from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = Product
        exclude = ('category',)
