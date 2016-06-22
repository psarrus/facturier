from django.conf.urls import url
from views import ProductDetailJsonView,ProductListView,ProductCreateView,ProductUpdateView

urlpatterns = [
    url(r'^(?P<pk>[\w-]+)/json$', ProductDetailJsonView.as_view(), name='product-json-detail'),
    url(r'^list/$', ProductListView.as_view(), name='list-product'),
    url(r'^create/$', ProductCreateView.as_view(), name='create-product'),
    url(r'^(?P<pk>[0-9]+)/update$', ProductUpdateView.as_view(), name='update-product'),

]
