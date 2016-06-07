from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.template import RequestContext
from .forms import LoginForm, UserForm, UserProfileForm, ChangePasswordForm
from django.forms.utils import ErrorList
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def CheckCredential(request):
    if request.user.is_authenticated():
        form = UserProfileForm(request.POST or None, instance=request.user)
        return HttpResponseRedirect('profile', {'form': form })
        # return render_to_response('Profile.html', {
        #     'form': form,
        # }, context_instance=RequestContext(request))
    else:
        if request.method == 'GET':
            register_form = UserForm()
            login_form = LoginForm()
            return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                          context_instance=RequestContext(request))
        elif request.method == 'POST':
            login_form = LoginForm(request.POST)
            register_form = UserForm()
            if login_form.is_valid():
                userName = login_form.cleaned_data['username']
                passWord = login_form.cleaned_data['password']
                user = authenticate(username=userName, password=passWord)
                if user is not None:
                    # the password verified for the user
                    if user.is_active:
                        print("User is valid, active and authenticated")
                        login(request, user)
                        LoginForm.session = request.session
                        return redirect('purchaseApp.list_un_payed')
                    else:
                        errors = login_form._errors.setdefault("username", ErrorList())
                        errors.append(_("حساب کاربری شما غیر فعال است. لطفا با مدیر سیستم تماس حاصل نمایید."))
                        return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                                      context_instance=RequestContext(request))
                else:
                    # the authentication system was unable to verify the username and password
                    errors = login_form._errors.setdefault("username", ErrorList())
                    errors.append(_("نام کاربری یا کلیدواژه نادرست است."))
                    print(login_form.errors.as_data())
                    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                                  context_instance=RequestContext(request))
            else:
                print(login_form.errors.as_data())
                return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                              context_instance=RequestContext(request))


def RegisterUser(request):
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        login_form = LoginForm()
        if register_form.is_valid():
            flag = get_user_model().objects.filter(email=request.POST['email']).exists()
            if flag == True:
                errors = register_form._errors.setdefault("email", ErrorList())
                errors.append(_("آدرس ایمیل ورودی در سیستم وجود دارد. لطفا آدرس ایمیل دیگری وارد نمایید."))
                return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                              context_instance=RequestContext(request))
            if register_form.cleaned_data['password'] == register_form.cleaned_data['password_confirmation']:
                try:
                    password_validation.validate_password(register_form.cleaned_data['password'])
                    register_form.save()
    #                return render(request, 'CreateGroup.html')
                    message = (_("حساب کاربری شما با موفقیت ثبت شد."))
                    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form,'message': message },
                                  context_instance=RequestContext(request))


                except ValidationError as err:
                    errors = register_form._errors.setdefault("password", ErrorList())
                    errors.append('; '.join(err))
                    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                                  context_instance=RequestContext(request))

            else:
                errors = register_form._errors.setdefault("password", ErrorList())
                errors.append(_("کلیدواژه و تکرار آن باید یکسان باشند."))
                return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                              context_instance=RequestContext(request))
        else:
            return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                          context_instance=RequestContext(request))
    elif request.method == 'GET':
        register_form = UserForm()
        login_form = LoginForm()
        return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                      context_instance=RequestContext(request))


def index(request):
    if request.user.is_authenticated():
        form = UserProfileForm(request.POST or None, instance=request.user)
        return render_to_response('Profile.html', {
            'form': form,
        }, context_instance=RequestContext(request))
    register_form = UserForm()
    login_form = LoginForm()
    return render(request, 'index.html', {'register_form': register_form, 'login_form':login_form},context_instance=RequestContext(request))


@login_required
def user_profile(request):
    current_user = request.user
    form = UserProfileForm(request.POST or None, instance=current_user)
    if request.POST:
        if form.is_valid():
            if len(str(form.cleaned_data['debit_card'])) == 16 or form.cleaned_data['debit_card'] is None:
                 form.save()
                 message = "اطلاعات شما با موفقیت بروز شد .‍"
                 return render(request, 'Profile.html', {'form':form, 'message':message}, context_instance=RequestContext(request))
            else:
                errors = form._errors.setdefault("debit_card", ErrorList())
                errors.append('شماره کارت میبایست 16 رقم باشد.')
    return render_to_response('Profile.html', {
        'form': form,
    }, context_instance=RequestContext(request))



def change_password(request):
    form = ChangePasswordForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                request.user.set_password(form.cleaned_data['password'])
                request.user.save()
                update_session_auth_hash(request, request.user)
                message = "اطلاعات شما با موفقیت بروز شد .‍"
                return render(request, 'ChangePassword.html', {'form': form, 'message': message},
                              context_instance=RequestContext(request))
    return render_to_response('ChangePassword.html', {
            'form': form,
    }, context_instance=RequestContext(request))



def logout_user(request):
    logout(request)
    return redirect('/')