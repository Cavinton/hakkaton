from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import AddToCartForm, CheckoutForm
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('view_cart')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'product': product, 'form': form})

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, total_price=0)
            total_price = 0
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                total_price += item.get_total_price()
            order.total_price = total_price
            order.save()
            cart_items.delete()
            return redirect('order_success')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'cart_items': cart_items, 'form': form})

@login_required
def order_success(request):
    return render(request, 'order_success.html')