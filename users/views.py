# redirect fo rredirecting the pages
from django.shortcuts import render, redirect
# Not using this import
from django.contrib.auth.forms import UserCreationForm
# to print one time message just like toast in Android
from django.contrib import messages
# We have implemented our own Registration form by extending the default UserCreationForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import datetime

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # saves the data from the form
            form.save()
            # retrives the data of username
            username = form.cleaned_data.get('username')
            # sends messages as toaster
            messages.success(
                request, f'Account has been created { username }! ')
            # redirecting the page to Blog-home
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    
    return render(request, 'users/profile.html', {'title': 'Profile'})


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # sends messages as toaster
            messages.success(request, f'Account has been updated ! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update_user.html', context)
