from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from account.forms import SignInForm


from django.contrib.auth import logout

from django.views.generic import View

from account.forms import SignUpForm


class SignUpView(View):
    """ User registration view """

    template_name = "signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("account:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)


def signout(request):
    logout(request)
    return redirect("account:signin")


class SignInView(View):

    template_name = "inner-page.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # return redirect("buycoffee:home")
        context = {"form": forms}
        return render(request, self.template_name, context)
