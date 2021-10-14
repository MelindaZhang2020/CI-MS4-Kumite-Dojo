from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product, Variation
from .models import Bag, BagItem
from django.http import HttpResponse
from django.conf import settings
from decimal import Decimal
from django.contrib import messages


def _bag_id(request):
    """A view to get the bag id"""
    bag = request.session.session_key
    if not bag:
        bag = request.session.create()
    return bag


def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # get the product
    product_variation = []
    if request.method == "POST":
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value,
                )
                product_variation.append(variation)
            except:
                pass

    try:
        bag = Bag.objects.get(
            bag_id=_bag_id(request)
        )  # get the bag using bag_id present in the session

    except Bag.DoesNotExist:
        bag = Bag.objects.create(bag_id=_bag_id(request))
        bag.save()

    is_bag_item_exists = BagItem.objects.filter(product=product, bag=bag).exists()
    if is_bag_item_exists:
        bag_item = BagItem.objects.filter(product=product, bag=bag)  # get the bagitem
        # existing variations --> database
        # current variation   --> product_variation
        # item_id   --> database
        existing_variation_list = []
        id = []
        for item in bag_item:
            existing_variation = item.variations.all()
            existing_variation_list.append(list(existing_variation))
            id.append(item.id)

        if product_variation in existing_variation_list:
            # increase bagitem quantity
            index = existing_variation_list.index(product_variation)
            item_id = id[index]
            item = BagItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()
            messages.success(
                request,
                f"Added 1 {product_variation[0]} {product_variation[1]} {product.name} to your bag",
            )

        else:
            # create new bagitem
            item = BagItem.objects.create(product=product, quantity=1, bag=bag)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
            messages.success(
                request,
                f"Added 1 {product_variation[0]} {product_variation[1]} {product.name} to your bag",
            )

    else:
        bag_item = BagItem.objects.create(
            product=product,
            quantity=1,
            bag=bag,
        )
        if len(product_variation) > 0:
            bag_item.variations.clear()
            bag_item.variations.add(*product_variation)
        bag_item.save()
        messages.success(
            request,
            f"Added 1 {product_variation[0]} {product_variation[1]} {product.name} to your bag",
        )

    return redirect("view_bag")


def view_bag(
    request,
    total=0,
    quantity=0,
    bag_items=None,
):
    """A view that renders the bag contents page and calculate bag cost"""
    try:
        bag = Bag.objects.get(bag_id=_bag_id(request))
        bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += bag_item.product.price * bag_item.quantity
            quantity += bag_item.quantity

    except ObjectDoesNotExist:
        pass  # just ignore

    return render(request, "bag/bag.html")


def remove_from_bag(request, product_id, bag_item_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        bag_item = BagItem.objects.get(product=product, bag=bag, id=bag_item_id)
        if bag_item.quantity > 1:
            bag_item.quantity -= 1
            bag_item.save()
            messages.success(
                request,
                f"Removed 1 {product.name} to your bag",
            )
        else:
            bag_item.delete()
            messages.success(
                request,
                f"Removed 1 {product.name} to your bag",
            )
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)

    return redirect("view_bag")


def remove_bag_item(request, product_id, bag_item_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    bag_item = BagItem.objects.get(product=product, bag=bag, id=bag_item_id)
    bag_item.delete()
    messages.success(
        request,
        f"Removed 1 {product.name} from your bag",
    )
    return redirect("view_bag")
