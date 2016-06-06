from django.shortcuts import render
from .forms import AddPurchaseFrom
from django.utils.translation import ugettext_lazy as _


def list_un_payed_purchases(request):
    return request.method


def list_payed_purchases(request):
    pass


def add_purchases_form(request):
    if request.method == 'POST':
        return add_purchase(request)
    add_form = AddPurchaseFrom()
    return render(request, 'AddPurchase.html',
                  {'static': statics(), 'add_form': add_form})


def add_purchase(request):
    add_form = AddPurchaseFrom(request.POST)
    if add_form.is_valid():
        add_form.save()
        msg = _('purchase_added_successfully')
    else:
        msg = _('error_while_add_purchase')
    add_form = AddPurchaseFrom()
    return render(request, 'AddPurchase.html',
                  {'static': statics(), 'add_form': add_form, 'msg': msg})


def statics():
    return {'page_title': _('purchase_page_title'),
            'page_header': _('purchase_page_header'),
            'balance': 0}