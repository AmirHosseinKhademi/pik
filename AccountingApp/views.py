from django.shortcuts import render
from .forms import ChargeAccountForm

def accounting_index(request):
    form = ChargeAccountForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            modified_form = form.save(commit=False)
            modified_form.action = 1
            modified_form.save()
            message = 'حساب شما با موافقیت به مبلغ %s شارژ شد.' % form.cleaned_data['amount']
            return render(request, 'Accounting.html', {'form':form, 'message':message})

    return render(request, 'Accounting.html', {'form':form})