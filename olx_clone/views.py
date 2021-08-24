from django.db.models import Count
from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator

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
    cate = Category.objects.all()
    prod = None
    all_category = Category.objects.annotate(total_products=Count('product'))

    if Category.objects.filter(slug=category).exists():
        cat = Category.objects.filter(slug=category)
        prod = Product.objects.filter(category=cat[0])

    paginator = Paginator(prod, 10)
    page = request.GET.get('page')
    prod = paginator.get_page(page)

    context = {
        "category": cate,
        "products": prod,
        "all_category": all_category,
        "category_obj": cat[0],
    }
    return render(request, "all-classifieds.html", context)




