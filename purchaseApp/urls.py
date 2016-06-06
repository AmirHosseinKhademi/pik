from django.conf.urls import url
from .views import (add_purchases_form,
                    list_un_payed_purchases,
                    list_payed_purchases)


urlpatterns = [
    url(r'^add$', add_purchases_form, name='purchaseApp.add.form'),
    url(r'^unpayed$', list_un_payed_purchases, name='purchaseApp.list_un_payed'),
    url(r'^payed$', list_payed_purchases, name='purchaseApp.list_payed'),
]