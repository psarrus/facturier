from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView

urlpatterns = [
    url(r'^list/$', ClientListView.as_view(), name='list-client'),
    url(r'^(?P<pk>[\d]+)$', ClientDetailView.as_view(), name='detail-client'),
    url(r'^(?P<pk>[\d]+)/update$', ClientUpdateView.as_view(), name='update-client'),
    url(r'^create/$', ClientCreateView.as_view(), name='create-client'),
    # url(r"^list_pdf$", InvoicePDFView.as_view(),name="list-pdf"),
    # url(r"^pdf/(?P<pk>[\d]+)$", InvoiceDetailPDFView.as_view(), name='detail-pdf'),
    # url(r'^delivery/$', DeliveryMapView.as_view(), name='delivery-map'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
