from django.contrib.auth import login, logout
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash


from . import forms




# class DashboardPage(TemplateView):
#     template_name = "accounts/Dashboard.html"



class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('company:Dashboard'))
        else:
            return redirect(reverse('accounts:change-password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

