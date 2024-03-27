# authentication_app/views.py

from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard if the user is a superuser
                if user.is_superuser:
                    return redirect('dashboard')
                else:
                    # Redirect to another page if the user is not a superuser
                    return redirect('some_other_page')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.contrib.auth.models import User
from .models import MyDataModel

@permission_required('enroll.can_view_data')
def view_data(request):
    if request.user.has_perm('enroll.can_view_data'):
        user_data = MyDataModel.objects.filter(user=request.user)
        return render(request, 'view_data.html', {'user_data': user_data})
    else:
        return HttpResponse("You don't have permission to view this data.")


def custom_password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            # Redirect to the password reset done page
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, "password_reset.html", {'form': form})

def custom_password_reset_done(request):
    return render(request, "password_reset_done.html")

def custom_logout(request):
    logout(request)
    return redirect('login')