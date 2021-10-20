from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jc4yQIsWlOWHJCE5sw7fbssMob1LVCbeK3PU24v9yI7qsXGyE4Nblpx1r8RkLJTw7fpBrF7uDmqUpLwX2eR7dle00B3wLO7aV',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
