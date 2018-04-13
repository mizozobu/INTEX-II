from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from django.contrib.auth import authenticate, login
from account import ldap
# from account import createAdAccount as ca
from account import models as amod


@view_function
def process_request(request):
    form = LoginForm(request)
    if request.method == 'GET':
        request.session['redirect_to'] = request.GET.get('next', '')
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect(request.session['redirect_to'])

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
        try:
            activeDirectory = ldap.test_connection(self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        except Exception as e:
            activeDirectory = False
        if activeDirectory:
            u = amod.User.objects.all().filter(username=self.cleaned_data.get('username').title()).first()
            if u is not None:
                self.user = authenticate(username=u.email, password=self.cleaned_data.get('password'))
            else:
                self.user = None
        else:
            self.user = authenticate(email=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if ((self.user is None) and (activeDirectory is False)):
            raise forms.ValidationError('Invalid email or password.')
        return self.cleaned_data

    def commit(self):
        if (self.user is None) and (ldap.test_connection(self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))):
            self.user = ldap.createAdAccount(self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        login(self.request, self.user)
