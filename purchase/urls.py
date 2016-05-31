from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^payed/$', views.retrieve_all_payed_purchases, name='list'),
    url(r'^unpayed/$', views.retrieve_all_un_payed_purchases, name='list'),
    url(r'^add_form$', views.add_purchase_form, name='list'),
]