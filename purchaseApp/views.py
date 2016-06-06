from django.shortcuts import render
from .forms import AddPurchaseFrom
from purchaseApp.models import Portion
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def list_un_payed_purchases(request):
    portions = Portion.objects.filter(Q(status=False) and Q(user=request.user.id))
    return render(request, 'Purchases.html', {'portions': portions})


@login_required
def list_payed_purchases(request):
    portions = Portion.objects.filter(Q(status=True) and Q(user=request.user.id))
    return render(request, 'PurchaseHistory.html', {'portions': portions})


@login_required
def add_purchases_form(request):
    if request.method == 'POST':
        return add_purchase(request)
    add_form = AddPurchaseFrom()
    return render(request, 'AddPurchase.html',
                  {'add_form': add_form})


@login_required
def add_purchase(request):
    add_form = AddPurchaseFrom(request.POST)
    if add_form.is_valid():
        add_form.save()
        msg = 'خرید با موفقیت ایجاد شد.'
    else:
        msg = 'خطا در ثبت خرید.'
    add_form = AddPurchaseFrom()
    return render(request, 'AddPurchase.html',
                  {'add_form': add_form, 'msg': msg})
