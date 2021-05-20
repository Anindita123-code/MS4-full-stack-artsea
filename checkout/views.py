from django.shortcuts import render, redirect, reverse

from .forms import OrderForm
from .models import Order, OrderLineItem
from django.contrib import messages


def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "Currently there are no items in your bag")
        return redirect(reverse('workshops'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
