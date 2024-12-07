from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED

def get_product_list():
    if not CACHE_ENABLED:
        return Product.objects.all().filter(publish_status=True)
    else:
        key = "product_list"
        products = cache.get(key)
        if products is None:
            return products

def category_products(pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.all().filter(category=category)
    return products
