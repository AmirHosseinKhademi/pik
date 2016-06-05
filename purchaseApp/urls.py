from django.conf.urls import url
from .views import add_purchases_form


urlpatterns = [
    url(r'^add', add_purchases_form, name='purchaseApp.add.form'),
]