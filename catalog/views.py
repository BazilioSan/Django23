from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}, за Ваше сообщение! Наши специалисты свяжутся с Вами по указанному номеру телефона!")
    return render(request, "contacts.html")

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_details.html", context)
