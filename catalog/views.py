from django.shortcuts import render
from json_views.views import JSONDetailView
from models import Product

# Create your views here.
class ProductDetailJsonView(JSONDetailView):
    model = Product
