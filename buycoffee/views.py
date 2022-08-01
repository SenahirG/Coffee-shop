from django.shortcuts import render
from django.contrib import messages

from .forms import order_form


def home(request):
    return render(request, 'index.html')


def orders(request):
    form = order_form()

    if request.method == 'POST':
        print('hello')

        form = order_form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your order has been placed successfully')

    context = {'form': form}
    return render(request, 'order.html', context)
