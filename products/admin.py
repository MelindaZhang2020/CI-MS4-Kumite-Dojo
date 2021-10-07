from django.contrib import admin
from .models import Product, Category, ProductImage, Variation


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Category, CategoryAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ("product", "variation_category", "variation_value", "active")


admin.site.register(Variation, VariationAdmin)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = ("name", "stock", "price", "slug", "active")
    list_editable = ["price", "active"]
    list_filter = ["price", "category"]
    readonly_field = ["update", "timestamp"]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
