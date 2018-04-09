from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from account import models as m
import re
from django.contrib.auth import authenticate, login
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


@view_function
def process_request(request):
    form = SignupForm(request)
    if form.is_valid():
        #form.send_email()
        form.commit()
        return HttpResponseRedirect('/homepage/')

    context = {
        'form': form,
    }

    return request.dmp.render('signup.html', context)


class SignupForm(Formless):
    def init(self):
        self.fields['email'] = forms.EmailField(label="Email")
        self.fields['first_name'] = forms.CharField(label="First")
        self.fields['last_name'] = forms.CharField(label="Last")
        self.fields['birthdate'] = forms.DateField(
            label="Birth Date",
            widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
        self.fields['street_address'] = forms.CharField(label="Address")
        self.fields['city'] = forms.CharField(label="City")
        self.fields['state'] = forms.CharField(label="State")
        self.fields['zip'] = forms.CharField(label="Zip")
        self.fields['password'] = forms.CharField(
            label="Password",
            widget=forms.PasswordInput())
        self.fields['password_confirm'] = forms.CharField(
            label="Confirm Password",
            widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check if this email already exists
        users = m.User.objects.filter(email=email)
        if len(users) > 0:
            raise forms.ValidationError("The email is already used by another user.")
        return email

    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", pw):
            raise forms.ValidationError("The password needs to be 8 characters or longer and must contain an alphabet and a number")
        return pw

    def clean(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('password_confirm')
        if pw1 != pw2:
            raise forms.ValidationError('The passwords do not match.')

        return self.cleaned_data

    def commit(self):
        user = m.User()
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.birthdate = self.cleaned_data.get('birthdate')
        user.street_address = self.cleaned_data.get('street_address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.zip = self.cleaned_data.get('zip')
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid email or password.')
        login(self.request, self.user)

    def send_email(self):
        # from_email = "mycodesnippet.notification@gmail.com"
        from_email = "hamc.sub@gmail.com"
        to_email = self.cleaned_data.get('email')
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(from_email, "nanakuni0914")

        msg = MIMEMultipart()

        # read in body from text file
        textfile = 'account/media/email.html'
        with open(textfile) as fp:
            msg.attach(MIMEText(fp.read(), "html"))
        msg["Subject"] = "Put subject here"
        msg["From"] = from_email
        msg["To"] = to_email

        # send
        server.send_message(msg)

        # end
        server.quit()
