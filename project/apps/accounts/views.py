from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import PasswordResetForm


from . import forms


class MyAccountView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'my_account.html'
    form_class = forms.UpdateProfile
    success_url = reverse_lazy('')
    success_message = "Suas informações foram alteradas com sucesso."

    def get_object(self, queryset=None):
        return self.request.user

    def update_profile(request):
        args = {}

        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('update_profile_success'))
        else:
            form = UpdateProfile()

        args['form'] = form
        return render(request, 'my_account.html', args)


# class MyAccountProfilePictureView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'my_account_profile_picture.html'
#     form_class = forms.MyAccountProfilePictureForm
#     success_url = reverse_lazy('accounts:my_account_profile_picture')
#     success_message = "Sua foto foi alterada com sucesso."

#     def get_object(self, queryset=None):
#         return self.request.user

#     def get_initial(self):
#         obj = self.get_object()
#         if obj.profile_image == 0:
#             return {'use_profile_picture': True}
#         return {}


# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'