from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
    )
    list_editable = ["price", "rating"]
    list_filter = ["price", "category"]
    readonly_field = ["update", "timestamp"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
