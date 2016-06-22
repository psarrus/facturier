from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy,reverse
from json_views.views import JSONDetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from models import Product
from forms import ProductForm

# Create your views here.
class ProductDetailJsonView(JSONDetailView):
    model = Product

class ProductListView(ListView):
    model = Product
    template_name = "list_product.html"
    context_object_name = "products"
    queryset = Product.objects.all()

class ProductCreateView(CreateView):
    template_name = 'create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list-product')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = '__all__'
    success_url = reverse_lazy('list-product')
