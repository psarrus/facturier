from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from views import InvoiceListView, InvoiceDetailView,InvoiceCreateView,InvoicePDFView,InvoiceDetailPDFView,DeliveryMapView

urlpatterns = [
    url(r'^list/$', InvoiceListView.as_view(), name='list-fact'),
    url(r'^(?P<pk>[\d]+)$', InvoiceDetailView.as_view(), name='detail-fact'),
    url(r'^create/$', InvoiceCreateView.as_view(), name='create-fact'),
    url(r"^list_pdf$", InvoicePDFView.as_view(),name="list-pdf"),
    url(r"^pdf/(?P<pk>[\d]+)$", InvoiceDetailPDFView.as_view(), name='detail-pdf'),
    url(r'^delivery/$', DeliveryMapView.as_view(), name='delivery-map'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
