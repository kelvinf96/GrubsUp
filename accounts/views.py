from django.urls import reverse_lazy
from django.views import generic
from . import models as m
from django.contrib.auth import get_user_model
from . import forms

class SignUpView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
