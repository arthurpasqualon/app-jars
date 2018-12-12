from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .forms import UpdateProfileForm


# Create your views here.

class HomeView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    template_name = 'home.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('core:home')
    success_message = "Suas informações foram alteradas com sucesso."

    def get_object(self, queryset=None):
        return self.request.user

def Contact(request):    
    return render(request, 'contact.html')
