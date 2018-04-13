from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from django.contrib.auth import authenticate, login
from account import ldap


@view_function
def process_request(request):
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/')

    context = {
        'form': form,
    }

    return request.dmp.render('login.html', context)


class LoginForm(Formless):
    def init(self):
        self.fields['username'] = forms.CharField(label="Username or Email", required=True)
        self.fields['password'] = forms.CharField(
            label="Password",
            required=True,
            widget=forms.PasswordInput())

    def clean(self):
        self.user = authenticate(email=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        
        if ((self.user is None) and (ldap.auth_AD(self.cleaned_data.get('username'), password=self.cleaned_data.get('password')) is False)):
            raise forms.ValidationError('Invalid email or password.')
        elif ((self.user is None) and (ldap.auth_AD(self.cleaned_data.get('username'), password=self.cleaned_data.get('password')))):
            print(">>>>>>>>>>>>No user account, but is in AD")
        else:
            print(">>>>>>>>>>>>User account and is in AD!!!!!!!!!!")
        return self.cleaned_data

    def commit(self):
        if (self.user is None) and (ldap.auth_AD(self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))):
            HttpResponseRedirect('/acount/ad_signup/')
        else:
            login(self.request, self.user)
