from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import myForm, NewUserForm
from .models import std


def AddStd(request):
    form = myForm()
    if request.method == "POST":
        stdForm = myForm(request.POST)
        if stdForm.is_valid():
            stdForm.save()
            return redirect('all_std')
        messages.error(request, "Form Value is Not Valid")
    return render(request, 'StudForm.html', {'form': form})


def UpdateStd(request, pk):
    studUp = std.objects.get(id=pk)
    form = myForm(instance=studUp)
    if request.method == "POST":
        stdForm = myForm(request.POST, instance=studUp)
        if stdForm.is_valid():
            stdForm.save()
            return redirect('all_std')
            messages.success(request, "Update Record")
        messages.error(request, "Form Value is Not Valid")
    return render(request, 'StudForm.html', {'form': form})


def ShowAllStd(request):
    dispAll = std.objects.all()
    return render(request, 'DisplayRecord.html', {'dispAll': dispAll})


def DeleteStd(request, pk):
    std.objects.get(id=pk).delete()
    return redirect('all_std')


def RegisterForm(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def LoginForm(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("all_std")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def LogoutForm(request):
    logout(request)
    return redirect("login")
