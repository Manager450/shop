import rave_python
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import Product
from django.urls import reverse
from rave_python import Rave
from django.http import JsonResponse

def make_payment(request):
    rave = Rave(settings.FLUTTERWAVE_PUBLIC_KEY, settings.FLUTTERWAVE_SECRET_KEY)
    
    response = rave.Card.charge({
        "amount": 500,
        "currency": "GHS",
        "email": request.user.email,
        "phonenumber": request.user.phone,
    })
    
    return render(request, 'orders/payment_success.html', {'response': response})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)

    order = Order.objects.create(user=request.user, total_price=total_price)
    order.cart.set(cart_items)
    order.save()

    rave = Rave(settings.FLUTTERWAVE_PUBLIC_KEY, settings.FLUTTERWAVE_SECRET_KEY)
    
    payment_url = reverse('confirm_payment', kwargs={'order_id': order.id})

    return render(request, 'orders/checkout.html', {'order': order, 'payment_url': payment_url})

@login_required
def confirm_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    rave = Rave(settings.FLUTTERWAVE_PUBLIC_KEY, settings.FLUTTERWAVE_SECRET_KEY)
    
    response = rave.Card.charge({
        "amount": str(order.total_price),
        "currency": "GHS",
        "email": request.user.email,
        "phonenumber": request.user.phone,
    })

    if response["status"] == "success":
        order.payment_status = True
        order.save()
        Cart.objects.filter(user=request.user).delete()
        return render(request, 'orders/payment_success.html', {'order': order})
    
    return render(request, 'orders/payment_failed.html')
