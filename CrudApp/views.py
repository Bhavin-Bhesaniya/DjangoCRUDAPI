from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import myForm
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
