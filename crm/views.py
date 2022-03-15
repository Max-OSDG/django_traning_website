from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider

# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()

    return render(request, './index.html', {'slider_list': slider_list,
                                            })

def thanks_page (request):
    name = request.POST['name']
    nom = request.POST['phone']

    el = Order()
    el.order_name = name
    el.order_phone = nom
    el.save()

    return render(request, './Thanks_page.html', {'name': name, 'nom': nom })
