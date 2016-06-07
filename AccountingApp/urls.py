from django.conf.urls import url
from .views import accounting_index, accounting_charge, accounting_checkout

urlpatterns = [
    url(r'^$', accounting_index, name='accounting_index'),
    url(r'^charge$', accounting_charge, name='accounting_charge'),
    url(r'^checkout$', accounting_checkout, name='accounting_checkout'),
]