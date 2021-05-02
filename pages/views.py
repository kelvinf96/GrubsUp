from django.shortcuts import render
from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class HomePageView(TemplateView):
    template_name = 'homepage.html'


