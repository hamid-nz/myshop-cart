from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = request.session.get("cart_id")

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart:cart_detail")

def cart_detail(request):
    cart_id = request.session.get("cart_id")
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    else:
        cart = None
    return render(request, "cart/cart_detail.html", {"cart": cart})