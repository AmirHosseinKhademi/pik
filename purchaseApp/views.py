from django.shortcuts import render
from .forms import AddPurchaseFrom
from purchaseApp.models import Portion, Purchase
from django.db.models import Q
from UserApp.models import CustomizedUser
from django.contrib.auth.decorators import login_required


@login_required
def list_un_payed_purchases(request):
    portions = Portion.objects.filter(Q(status=False) & Q(user=request.user.id))
    return render(request, 'Purchases.html', {'portions': portions})


@login_required
def list_payed_purchases(request):
    portions = Portion.objects.filter(Q(status=True) & Q(user=request.user.id))
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
        added_purchase = Purchase.objects.create_purchase(
            title=add_form.cleaned_data.get('title'),
            price=add_form.cleaned_data.get('price'),
            group=add_form.cleaned_data.get('group')
        )
        users_portions = dict((CustomizedUser.objects.get(pk=key.split(':')[1]), int(value))
                              for (key, value) in request.POST.items()
                              if key.startswith('portion') and int(value) >= 0)
        if len(users_portions) < len(added_purchase.group.member.all()):
            msg = 'خطا در ثبت خرید لطفا اطلاعات را با دقت وارد کنید.'
        else:
            for user, amount in users_portions.items():
                Portion.objects.create_portion(user=user, purchase=added_purchase, amount=amount)
            msg = 'خرید با موفقیت ایجاد شد.'
    else:
        msg = 'خطا در ثبت خرید.'
    add_form = AddPurchaseFrom()
    return render(request, 'AddPurchase.html',
                  {'add_form': add_form, 'msg': msg})
