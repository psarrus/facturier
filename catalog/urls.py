from django.conf.urls import url
from views import ProductDetailJsonView

urlpatterns = [
    url(r'^(?P<pk>[\w-]+)/json$', ProductDetailJsonView.as_view(), name='product-json-detail'),
]
