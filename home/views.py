from django.shortcuts import render
from products.models import Product


def index(request):
    """A view to return the index page"""
    products = Product.objects.filter(is_featured=True).order_by("-id")
    return render(request, "home/index.html", {"products": products})
