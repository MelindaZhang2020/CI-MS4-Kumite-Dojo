from django.shortcuts import render
from products.models import Product
from .models import Banner


def index(request):
    """A view to return the index page"""
    banners = Banner.objects.all().order_by("-id")
    products = Product.objects.filter(is_featured=True).order_by("-id")
    context = {
        "products": products,
        "banners": banners,
    }
    return render(request, "home/index.html", context)
