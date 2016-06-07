from django.shortcuts import render
from .forms import ChargeAccountForm, CheckoutForm
from django.forms.utils import ErrorList
from UserApp.models import CustomizedUser
from .models import AccountingModel


def accounting_index(request):
    charge_form = ChargeAccountForm(request.POST or None)
    checkout_form = CheckoutForm(request.POST or None)
    transactions = AccountingModel.objects.filter(user=request.user)
    return render(request, 'Accounting.html',
                  {'charge_form':charge_form, 'checkout_form':checkout_form, 'transactions':transactions}
                  )


def accounting_charge(request):
    charge_form = ChargeAccountForm(request.POST or None)
    checkout_form = CheckoutForm()
    if request.POST:
        if charge_form.is_valid():
            amount = charge_form.cleaned_data['amount']
            if amount != 0 :
                modified_form = charge_form.save(commit=False)
                modified_form.action = 1
                modified_form.user = request.user
                modified_form.portion = None
                modified_form.save()
                current_user = CustomizedUser.objects.get(email=request.user.email)
                current_user.balance += amount
                current_user.save()
                charge_message = 'حساب شما با موافقیت به مبلغ %s شارژ شد.' % charge_form.cleaned_data['amount']
                return render(request, 'Accounting.html',
                              {'charge_form': charge_form, 'checkout_form': checkout_form, 'charge_message':charge_message}
                              )
            else:
                errors = charge_form._errors.setdefault("amount", ErrorList())
                errors.append('مبلغ شارژ میبایست بزرگ تر از صفر باشد')
    return render(request, 'Accounting.html',
                  {'charge_form': charge_form, 'checkout_form': checkout_form}
                  )


def accounting_checkout(request):
    print('enter')
    charge_form = ChargeAccountForm()
    checkout_form = CheckoutForm(request.POST or None)
    if request.POST:
        if checkout_form.is_valid():
            amount = checkout_form.cleaned_data['amount']
            modified_form = checkout_form.save(commit=False)
            modified_form.action = 2
            modified_form.user = request.user
            modified_form.portion = None
            current_user = CustomizedUser.objects.get(email=request.user.email)
            if amount != 0:
                if amount <= current_user.balance :
                    if current_user.debit_card is not None:
                        modified_form.save()
                        current_user.balance -= amount
                        current_user.save()
                        checkout_message = 'درخواست تسویه شما به مبلغ %s ثبت گردید.' % checkout_form.cleaned_data['amount']
                        return render(request, 'Accounting.html',
                                      {'charge_form': charge_form, 'checkout_form': checkout_form, 'checkout_message': checkout_message}
                                      )
                    else:
                        errors = checkout_form._errors.setdefault("amount", ErrorList())
                        errors.append('ابتدا از طریق بروفایل شماره کارت اعتباری خود را وارد نمایید.')
                else:
                    errors = checkout_form._errors.setdefault("amount", ErrorList())
                    errors.append('مبلغ درخواستی بیشتر از موجودی است.')
            else:
                errors = checkout_form._errors.setdefault("amount", ErrorList())
                errors.append('مبلغ درخواست میبایست بزرگ تر از صفر باشد')
    return render(request, 'Accounting.html',
                  {'charge_form': charge_form, 'checkout_form': checkout_form}
                  )