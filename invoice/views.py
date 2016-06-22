from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse_lazy,reverse
from models import Invoice, InvoiceLine
from customer.models import Address
from django.forms import inlineformset_factory
from forms import InvoiceLineFormSet
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from easy_pdf.views import PDFTemplateView

class InvoiceListView(ListView):
    model = Invoice
    template_name = "list_invoice.html"
    context_object_name = "invoices"
    queryset = Invoice.objects.all()

class InvoicePDFView(PDFTemplateView):
    template_name = "list_invoice_pdf.html"

    def get_context_data(self, **kwargs):
        invoices = Invoice.objects.all()
        return super(InvoicePDFView, self).get_context_data(
                                                            pagesize="A4",
                                                            title="Liste des factures",
                                                            invoices=invoices,
                                                            **kwargs
                                                            )

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "detail_invoice.html"
    context_object_name = "invoice"

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        context["invoicelines"] = self.get_object().invoiceline_set.all()
        return context

class InvoiceDetailPDFView(PDFTemplateView):
    template_name = "detail_invoice_pdf.html"

    def get_context_data(self, **kwargs):
        invoice =  get_object_or_404(Invoice,pk=self.kwargs['pk'])
        return super(InvoiceDetailPDFView, self).get_context_data(pagesize="A4",
                                                                invoice=invoice
                                                                )



class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'create_invoice.html'
    fields = '__all__'
    success_url = reverse_lazy('list-fact')

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        # context ['address'] = AdresseLineFormSet()
        context ["invoiceline_formset"] = InvoiceLineFormSet()
        return context


    def form_valid(self, form):
        invoiceline_formset = InvoiceLineFormSet(self.request.POST)
        if form.is_valid() and invoiceline_formset.is_valid():
            invoice = form.save()
            invoiceline_formset = InvoiceLineFormSet(self.request.POST,instance=invoice)
            invoiceline_formset.is_valid()
            invoiceline_formset.save()
            return redirect(reverse('detail-fact',args=[invoice.id]))
        return self.render_to_response(self.get_context_data(form=form))


class DeliveryMapView(TemplateView):
   template_name = "delivery_map.html"
   def get_context_data(self, **kwargs):
       context = super(DeliveryMapView, self).get_context_data(**kwargs)
       context['addresses'] = Address.objects.all()
       return context
