from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from users.models import CustomUser
from users.forms import LoginForm, CustomUserCreationForm


# Create your views here.

class RegistrationView(View):
    template_name = "user/registration.html"

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name = "user/login.html"
    model = CustomUser

    def get(self, request, *args, **kwargs):
        form = LoginForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("correct", form.cleaned_data)
        return render(request, self.template_name, {'form': form})
