from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    return render(request, "index.html")


def productDetail(request, product_slug):
    product = Product.objects.filter(slug=product_slug)
    context = {"prod": product}
    return render(request, "detail.html", context)