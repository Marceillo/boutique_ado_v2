from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reverse('product'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
        
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q3EasG1ZGJMpzARnGbA5tkDKLEwfOlpA20kPlwXt52PN660w3qYOHL6jeoZDo8GbxfwV8r8IHU8XNcL18OAbZTb00ewqNwwtf',
        'client_secret': 'test client secret',        
    }

    return render (request, template, context)
