from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
# Create your views here.

class PasswordChangeView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'

class SignUpView(CreateView):
    template_name = "registration/password_change_done.html"
# Create your views here.

class PasswordResetView(FormView):
    template_name = 'registration/password_reset_form.html'