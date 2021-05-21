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
        'stripe_public_key': "pk_test_51IhatxHqVn8XUqr5sF2YPaAUovt90NvX254lggWcTnFGTkOUesBfgGZfO33JVj7unC4RfguQUJVs5E9auCBzmMt500ivCvwLaZ",
        'client_secret': 'this is a secret code',
    }
    return render(request, template, context)