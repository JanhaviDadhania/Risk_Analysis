from django.shortcuts import render
from .forms import transplant_form, death_form
from django.contrib import messages

# Create your views here.
def transplant(request):
    if request.method == 'POST':
        form = transplant_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your response is successfuly saved. Thank you !')
        else:
            print(form.errors)
            messages.error(request, "Couldn't save your response. Please try again.")
    form = transplant_form()
    return render(request, 'pages/transplant.html', {'form':form})

def death(request):
    if request.method == 'POST':
        form = death_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your response is successfuly saved. Thank you !')
        else:
            print(form.errors)
            messages.error(request, "Couldn't save your response. Please try again.")
    form = death_form()
    return render(request, 'pages/death.html', {'form':form})
