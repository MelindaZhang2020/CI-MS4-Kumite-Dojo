from django.db import models

# Category
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        unique_together = ("name", "slug")

    def __str__(self):
        return self.name


# Product Images
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products_imgs/", null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.image


# Variation Manager
class VariationManager(models.Manager):
    use_in_migrations = True

    def colors(self):
        return super(VariationManager, self).filter(
            variation_category="color", active=True
        )

    def sizes(self):
        return super(VariationManager, self).filter(
            variation_category="size", active=True
        )


# Variation
variation_category_choice = (
    ("color", "color"),
    ("size", "size"),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice
    )
    variation_value = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
