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


def contact(request):
    """A view to return the contact page"""
    return render(request, "home/contact.html")


def about(request):
    """A view to return the about page"""
    return render(request, "home/about.html")
