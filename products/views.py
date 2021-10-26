from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductImage, Variation
from bag.models import BagItem
from bag.views import _bag_id
from django.http import HttpResponse
from .forms import ProductForm, ProductImageForm, ProductVariationForm
from django.contrib.auth.decorators import login_required


def all_products(request, category_name=None):
    """A view to show all products, including sorting and search quries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey == "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
                products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criterial")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_slug):
    """A view to show individual product details"""

    product = get_object_or_404(Product, slug=product_slug)
    in_bag = BagItem.objects.filter(
        bag__bag_id=_bag_id(request), product=product
    ).exists()

    context = {
        "product": product,
        "in_bag": in_bag,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        product_variation_form = ProductVariationForm(request.POST, request.FILES)
        if (
            product_form.is_valid()
            and product_image_form.is_valid()
            and product_variation_form.is_valid()
        ):
            product = product_form.save()
            product_image = ProductImage(
                product=product,
                image=product_image_form.cleaned_data["image"],
                featured=product_image_form.cleaned_data["featured"],
                active=product_image_form.cleaned_data["active"],
            )
            product_image.save()
            product_variation = Variation(
                product=product,
                variation_category=product_variation_form.cleaned_data[
                    "variation_category"
                ],
                variation_value=product_variation_form.cleaned_data["variation_value"],
            )
            product_variation.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.slug]))

        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        product_form = ProductForm()
        product_image_form = ProductImageForm()
        product_variation_form = ProductVariationForm()
    template = "products/add_product.html"
    context = {
        "product_form": product_form,
        "product_image_form": product_image_form,
        "product_variation_form": product_variation_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product_image = get_object_or_404(ProductImage, product__pk=product_id)
    product_variation = get_object_or_404(Variation, product__pk=product_id)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        product_image_form = ProductImageForm(
            request.POST, request.FILES, instance=product
        )
        product_variation_form = ProductVariationForm(
            request.POST, request.FILES, instance=product
        )
        if (
            product_form.is_valid()
            and product_image_form.is_valid()
            and product_variation_form.is_valid()
        ):
            product_form.save()
            product_image_form.save()
            product_variation_form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.slug]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        product_form = ProductForm(instance=product)
        product_image_form = ProductImageForm(instance=product_image)
        product_variation_form = ProductVariationForm(instance=product_variation)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "product_form": product_form,
        "product": product,
        "product_image_form": product_image_form,
        "product_variation_form": product_variation_form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
