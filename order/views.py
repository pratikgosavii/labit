from django.shortcuts import render

# Create your views here.



from .models import *
from masters.models import *


def apply_coupon(cart_total, coupon_code):
    try:
        coupon_instance = coupon.objects.get(code=coupon_code, is_active=True, start_date__lte=now(), end_date__gte=now())
    except coupon.DoesNotExist:
        return {"error": "Invalid or expired coupon"}

    if cart_total < coupon_instance.min_purchase:
        return {"error": f"Minimum purchase required: ₹{coupon_instance.min_purchase}"}

    # Calculate discount
    if coupon_instance.discount_percentage:
        discount = (cart_total * coupon_instance.discount_percentage) / 100
    else:
        discount = coupon_instance.discount_amount

    # Apply max discount limit
    if coupon_instance.max_discount and discount > coupon_instance.max_discount:
        discount = coupon_instance.max_discount

    final_price = cart_total - discount

    return {
        "discount": discount,
        "final_price": final_price,
        "message": f"coupon applied successfully! Discount: ₹{discount}"
    }



from django.contrib.contenttypes.models import ContentType

def add_to_cart(user, item):
    content_type = ContentType.objects.get_for_model(item)
    cart_item, created = cart.objects.get_or_create(user=user, content_type=content_type, object_id=item.id)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return cart_item


def get_cart_items(user):
    cart_items = cart.objects.filter(user=user)
    
    medicine_items = []
    test_items = []

    for item in cart_items:
        if item.content_type.model == "medicine":
            medicine_items.append(item)
        elif item.content_type.model == "test":
            test_items.append(item)

    return {'medicines': medicine_items, 'tests': test_items}
