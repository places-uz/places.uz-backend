from django.contrib import admin

from places.models import Place
from products.models import Product, Category

admin.site.register([Place, Product, Category])
