from django.shortcuts import render
from .models import Product, ProductImages, Category


# Create your views here.
def index(request):
    return render(request, "index.html")


def productDetail(request, product_slug):
    product = Product.objects.filter(slug=product_slug)
    prod_img = ProductImages.objects.filter(product=product[0])
    context = {
        "prod": product,
        "prod_img": prod_img
    }
    return render(request, "detail.html", context)


def category(request):
    cate = Category.objects.all()
    context = {"category": cate}
    return render(request, 'categories.html', context)