from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Client, Address

# Create your views here.
class ClientListView(ListView):
    model = Client
    template_name = "list_client.html"
    context_object_name = "clients"
    queryset = Client.objects.all()

class ClientDetailView(DetailView):
    model = Client
    template_name = "detail_client.html"
    context_object_name = "client"

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context["address"] = self.get_object().clientaddress_set.all()
        return context

class ClientCreateView(CreateView):
    template_name = "create_client.html"
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('list-client')
