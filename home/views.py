from django.shortcuts import render, redirect, reverse
from products.models import Product
from .models import Banner, Contact
from django.contrib import messages


def index(request):
    """A view to return the index page"""
    banners = Banner.objects.all().order_by("-id")
    products = Product.objects.filter(is_featured=True).order_by("-id")
    context = {
        "products": products,
        "banners": banners,
    }
    return render(request, "home/index.html", context)


def about(request):
    """A view to return the about page"""
    return render(request, "home/about.html")


def classes(request):
    """A view to return the classes page"""
    return render(request, "home/classes.html")


def contact_submit(request):
    """A view to return the contact page"""
    if request.method == "POST":
        contact = Contact()
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.message = message
        contact.save()
        messages.success(
            request,
            f"Your message has been sent, thank you for contacting us!",
        )
    return redirect(reverse("home"))


def contact_form(request):
    """A view to render the contact form page"""
    return render(request, "home/contact.html")
