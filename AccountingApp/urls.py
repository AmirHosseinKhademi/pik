from django.conf.urls import url
from .views import accounting_index

url(r'^$', accounting_index, name='accounting_index'),
