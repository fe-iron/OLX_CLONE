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


def allCategory(request, category):
    category = category.capitalize()
    cate = Category.objects.all()
    prod = None
    if Category.objects.filter(name=category).exists():
        cat = Category.objects.filter(name=category)
        prod = Product.objects.filter(category=cat[0])

    context = {
        "category": cate,
        "products": prod,
    }
    return render(request, "all-classifieds.html", context)




