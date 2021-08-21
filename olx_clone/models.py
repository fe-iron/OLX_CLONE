from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify


class Product(models.Model):
    '''
        desc: This class contains all the information about the Products
    '''

    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True, null=True)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    image = models.ImageField(upload_to='main_product/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    '''
    desc: This model is for all the category of OLX
    '''

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', blank=True, null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Brand(models.Model):
    '''
    desc: This model is for all the Brand of the  categories
    '''

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
