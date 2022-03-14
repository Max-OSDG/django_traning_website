from django.shortcuts import render
from .models import Order

# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})

def thanks_page (request):
    name = request.GET ['name']
    nom = request.GET ['nomer']

    el = Order()
    el.order_name = name
    el.order_phone = nom
    el.save()

    return render(request, './Thanks_page.html', {'name': name, 'nom': nom })
