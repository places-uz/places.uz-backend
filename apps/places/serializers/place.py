from rest_framework import serializers
from products.serializers.category import CategorySerializer
from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)
    cover = serializers.ImageField(required=False)
    categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Place
        fields = ['name', 'url', 'currency', 'main_language', 'logo', 'cover', 'phone',
                  'wifi_password', 'address', 'information', 'work_hours_from', 'work_hours_to', 'theme', 'categories']

    def get_categories(self, obj):
        return CategorySerializer(obj.categories, many=True).data
