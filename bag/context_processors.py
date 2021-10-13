from .models import Bag, BagItem
from .views import _bag_id
from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product, Variation


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    if Bag.objects.filter(bag_id=_bag_id(request)):
        bag = Bag.objects.filter(bag_id=_bag_id(request))[0]
        bag_items = BagItem.objects.all().filter(bag=bag)
        for bag_item in bag_items:
            print("Bag Item ", bag_item)
            total = total + bag_item.sub_total()

        product_count = len(bag_items)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
