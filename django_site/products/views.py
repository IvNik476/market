from django.views import generic

from .models import Product

from .models import Category
class IndexView(generic.ListView):

    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product

class CategoryDetailView(generic.DetailView):
    template_name = 'category_detail.html'
    model = Category