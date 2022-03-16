from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table}
    return render(request, './index.html', dict_obj )

def thanks_page (request):
    name = request.POST['name']
    nom = request.POST['phone']

    el = Order()
    el.order_name = name
    el.order_phone = nom
    el.save()

    return render(request, './Thanks_page.html', {'name': name, 'nom': nom })
