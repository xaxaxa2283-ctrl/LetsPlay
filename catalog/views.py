from django.shortcuts import render
from .models import Catalog
from django.views.generic import DetailView

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Order, Catalog

# Create your views here.
def catalog(request):
    catalogs = Catalog.objects.all()
    return render(request,'catalog/catalog.html',{'catalogs':catalogs})


class CatalogDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/catalog_detail.html'
    context_object_name = 'catalog'






'''
@require_POST
def buy_product(request, product_id):
    product = get_object_or_404(Catalog, id=product_id)
    name = request.POST.get('name')
    phone = request.POST.get('phone')

    Order.objects.create(name=name, phone=phone, product=product)

    return redirect('thank_you')




def thank_you(request):
    return render(request, 'catalog/thank_you.html')'''




import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Order, Catalog

def buy_product_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        phone = data.get("phone")
        product_id = data.get("product_id")
        product_id = data.get("product_id")
        product = get_object_or_404(Catalog, id=product_id)

        Order.objects.create(name=name, phone=phone, product=product)

        return JsonResponse({"status": "ok", "message": "Спасибо! Мы свяжемся с вами в ближайшее время."})

    return JsonResponse({"status": "error", "message": "Ошибка при отправке."}, status=400)




