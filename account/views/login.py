from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from django.contrib.auth import authenticate, login


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
        self.fields['email'] = forms.EmailField(label="Email", required=True)
        self.fields['password'] = forms.CharField(
            label="Password",
            required=True,
            widget=forms.PasswordInput())

    def clean(self):
        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid email or password.')
        return self.cleaned_data

    def commit(self):
        login(self.request, self.user)
