from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from models import Client, Address
from forms import *

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
        context["addresslines"] = self.get_object().address_set.all()
        return context

class ClientCreateView(CreateView):
    # model = Client
    template_name = "create_client.html"
    form_class = ClientForm
    success_url = reverse_lazy('list-client')

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['addressline_formset'] = AddressLineFormSet()
        return context

    def form_valid(self, form):
        print self.request.POST
        addressline_formset = AddressLineFormSet(self.request.POST)
        if form.is_valid() and addressline_formset.is_valid():
            client = form.save()
            addressline_formset = AddressLineFormSet(self.request.POST,instance=client)
            addressline_formset.is_valid()
            addressline_formset.save()
            return redirect(reverse('list-client'))
        return self.render_to_response(self.get_context_data(form=form))

class ClientUpdateView(UpdateView):
    template_name = "update_client.html"
    form_class = ClientForm
    success_url = reverse_lazy('list-client')

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['addressline_formset'] = AddressLineFormSet()
        return context

    def form_valid(self, form):
        addressline_formset = AddressLineFormSet(self.request.POST)
        if form.is_valid() and addressline_formset.is_valid():
            client = form.save()
            addressline_formset = AddressLineFormSet(self.request.POST,instance=client)
            addressline_formset.is_valid()
            addressline_formset.save()
            return redirect(reverse('list-client'))
        return self.render_to_response(self.get_context_data(form=form))
