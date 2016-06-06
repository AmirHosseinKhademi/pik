from django.shortcuts import render
from .forms import ChargeAccountForm, CheckoutForm

def accounting_index(request):
    charge_form = ChargeAccountForm(request.POST or None)
    checkout_form = CheckoutForm(request.POST or None)
    return render(request, 'Accounting.html', {'charge_form':charge_form, 'checkout_form':checkout_form})

def accounting_charge(request):
    charge_form = ChargeAccountForm(request.POST or None)
    checkout_form = CheckoutForm()
    if request.POST:
        if charge_form.is_valid():
            modified_form = charge_form.save(commit=False)
            modified_form.action = 1
            modified_form.user = request.user
            modified_form.portion = None
            modified_form.save()
            charge_message = 'حساب شما با موافقیت به مبلغ %s شارژ شد.' % charge_form.cleaned_data['amount']
            return render(request, 'Accounting.html',
                          {'charge_form': charge_form, 'checkout_form': checkout_form, 'charge_message':charge_message}
                          )

    return render(request, 'Accounting.html', {'charge_form': charge_form, 'checkout_form': checkout_form})