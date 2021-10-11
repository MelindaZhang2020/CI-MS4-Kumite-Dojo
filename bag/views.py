from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from .models import Bag, BagItem
from django.http import HttpResponse
from django.conf import settings
from decimal import Decimal


def _bag_id(request):
    """A view to get the bag id"""
    bag = request.session.session_key
    if not bag:
        bag = request.session.create()
    return bag


def add_to_bag(request, product_id):
    product = Product.objects.get(id=product_id)  # get the product
    try:
        bag = Bag.objects.get(
            bag_id=_bag_id(request)
        )  # get the bag using bag_id present in the session

    except Bag.DoesNotExist:
        bag = Bag.objects.create(bag_id=_bag_id(request))
        bag.save()

    try:
        bag_item = BagItem.objects.get(product=product, bag=bag)  # get the bagitem
        bag_item.quantity += 1
        bag_item.save()

    except BagItem.DoesNotExist:
        bag_item = BagItem.objects.create(
            product=product,
            quantity=1,
            bag=bag,
        )
        bag_item.save()
    return redirect("view_bag")


def view_bag(request, total=0, quantity=0, bag_items=None):
    """A view that renders the bag contents page and calculate bag cost"""
    try:
        bag = Bag.objects.get(bag_id=_bag_id(request))
        bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += bag_item.product.price * bag_item.quantity
            quantity += bag_item.quantity
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        else:
            delivery = 0
            free_delivery_delta = 0
        grand_total = delivery + total

    except ObjectDoesNotExist:
        pass  # just ignore

    context = {
        "total": total,
        "quantity": quantity,
        "bag_items": bag_items,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "grand_total": grand_total,
    }
    return render(request, "bag/bag.html", context)


def remove_from_bag(request, product_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    bag_item = BagItem.objects.get(product=product, bag=bag)
    if bag_item.quantity > 1:
        bag_item.quantity -= 1
        bag_item.save()
    else:
        bag_item.delete()
    return redirect("view_bag")


def remove_bag_item(request, product_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    bag_item = BagItem.objects.get(product=product, bag=bag)
    bag_item.delete()
    return redirect("view_bag")


# def add_to_bag(request, item_id):
#     """Add a quantity of the specified product to the shopping bag"""

#     quantity = int(request.POST.get("quantity"))
#     redirect_url = request.POST.get("redirect_url")
#     size = None
#     if "product_size" in request.POST:
#         size = request.POST["product_size"]
#     bag = request.session.get("bag", {})

#     if size:
#         if item_id in list(bag.keys()):
#             if size in bag[item_id]["items_by_size"].keys():
#                 bag[item_id]["items_by_size"][size] += quantity
#             else:
#                 bag[item_id]["items_by_size"][size] = quantity
#         else:
#             bag[item_id] = {"items_by_size": {size: quantity}}
#     else:
#         if item_id in list(bag.keys()):
#             bag[item_id] += quantity
#         else:
#             bag[item_id] = quantity

#     request.session["bag"] = bag
#     return redirect(redirect_url)


# def adjust_bag(request, item_id):
#     """Adjust the quantity of the specified product to the specified amount"""

#     quantity = int(request.POST.get("quantity"))
#     size = None
#     if "product_size" in request.POST:
#         size = request.POST["product_size"]
#     bag = request.session.get("bag", {})

#     if size:
#         if quantity > 0:
#             bag[item_id]["items_by_size"][size] = quantity
#         else:
#             del bag[item_id]["items_by_size"][size]
#             if not bag[item_id]["items_by_size"]:
#                 bag.pop(item_id)
#     else:
#         if quantity > 0:
#             bag[item_id] = quantity
#         else:
#             bag.pop(item_id)
#     request.session["bag"] = bag
#     return redirect(reverse("view_bag"))


# def remove_from_bag(request, item_id):
#     """Remove the item from the shopping bag"""
#     try:
#         size = None
#         if "product_size" in request.POST:
#             size = request.POST["product_size"]
#         bag = request.session.get("bag", {})
#         if size:
#             del bag[item_id]["items_by_size"][size]
#             if not bag[item_id][items_by_size]:
#                 bag.pop(item_id)
#         else:
#             bag.pop(item_id)
#         request.session["bag"] = bag
#         return HttpResponse(status=200)
#     except Exception as e:
#         return HttpResponse(status=500)
