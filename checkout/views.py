from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from bag.views import _bag_id
from bag.models import Bag
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.session_key
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": "test client secret",
    }

    return render(request, template, context)
