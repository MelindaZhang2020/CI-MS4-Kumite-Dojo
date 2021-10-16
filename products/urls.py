from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("products/<slug>", views.product_detail, name="product_detail"),
    path("<category_name>", views.all_products, name="products_by_category"),
]
