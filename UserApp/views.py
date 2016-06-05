from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.template import RequestContext
from .forms import LoginForm, UserForm, UserProfileForm, ChangePasswordForm
from django.http.response import HttpResponseRedirect
from django.forms.utils import ErrorList
from django.contrib.auth import password_validation
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect

# Create your views here.

def CheckCredential(request):
    if request.method == 'GET':
        register_form = UserForm()
        login_form = LoginForm()
        return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                      context_instance=RequestContext(request))
    elif request.method == 'POST':
        if request.user.is_authenticated():
            logout(request)
            register_form = UserForm()
            login_form = LoginForm()
            return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                          context_instance=RequestContext(request))
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
                    # return HttpResponseRedirect('Purchases.html')
                    return render(request, 'Purchases.html')
                else:
                    errors = login_form._errors.setdefault("username", ErrorList())
                    errors.append(u"The password is valid, but the account has been disabled!")
                    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                                  context_instance=RequestContext(request))
            else:
                # the authentication system was unable to verify the username and password
                errors = login_form._errors.setdefault("username", ErrorList())
                errors.append(u"The username or password was incorrect.")
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
                errors.append(u"This email exists. Please try another one.")
                return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                              context_instance=RequestContext(request))
            if register_form.cleaned_data['password'] == register_form.cleaned_data['password_confirmation']:
                try:
                    flag_err = password_validation.validate_password(register_form.cleaned_data['password'])
                    register_form.save()
                    return HttpResponseRedirect('../CreateGroup.html')
                except ValidationError as err:
                    errors = register_form._errors.setdefault("password", ErrorList())
                    errors.append('; '.join(err))
                    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form},
                                  context_instance=RequestContext(request))

            else:
                errors = register_form._errors.setdefault("password", ErrorList())
                errors.append(u"password and password confirmation should be the same.")
                print(register_form.errors.as_data())
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
    register_form = UserForm()
    login_form = LoginForm()
    return render(request, 'index.html', {'register_form': register_form, 'login_form':login_form},context_instance=RequestContext(request))


def user_profile(request):
    current_user = request.user
    form = UserProfileForm(request.POST or None, instance=current_user)
    if request.POST:
        if form.is_valid():
             # pwd = form.cleaned_data['password']
             # form_obj = form.save(commit=False)
             # form_obj.password = make_password(pwd)
             form.save()
             # update_session_auth_hash(request, current_user)
             message = "اطلاعات شما با موفقیت بروز شد .‍"
             return render(request, 'Profile.html', {'form':form, 'message':message}, context_instance=RequestContext(request))

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