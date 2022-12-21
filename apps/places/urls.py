from django.urls import path
from products.views.product import ProductsListView, ProductsDetailView
from products.views.category import CategoriesListView, CategoriesDetailView
from places.views.place import PlacesListView, PlacesDetailView

urlpatterns = [
    path('', PlacesListView.as_view()),
    path('<str:place_url>', PlacesDetailView.as_view()),
    path('<str:place_url>/categories', CategoriesListView.as_view()),
    path('<str:place_url>/categories/<int:category_id>',
         CategoriesDetailView.as_view()),
    path('<str:place_url>/categories/<int:category_id>/products',
         ProductsListView.as_view()),
    path('<str:place_url>/categories/<int:category_id>/products/<int:product_id>',
         ProductsDetailView.as_view()),
]
