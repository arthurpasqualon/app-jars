from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
def Contact(request):    
    return render(request, 'contact.html')
