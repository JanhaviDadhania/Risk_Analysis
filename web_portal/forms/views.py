from django.shortcuts import render
from .forms import transplant_form, death_form
from django.contrib import messages
from subprocess import run, PIPE
import sys

# Create your views here.
def transplant(request):
    if request.method == 'POST':
        form = transplant_form(request.POST)
        if form.is_valid():
            form.save()
            # print(type(form.cleaned_data.values()))
            #input is list that stores the values submitted by user
            input = []
            for item in form.cleaned_data.values():
                print(item)
                input.append(item)
            temp = ' '.join([str(elem) for elem in input])
            output = run([sys.executable, '//home//janhavi//django//nnn//Risk_Analysis//web_portal//forms//ML//transplant_model.py', temp], shell=False, stdout=PIPE)
            messages.success(request, output.stdout)
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
            # print(type(form.cleaned_data.values()))
            #input is list that stores the values submitted by user
            input = []
            for item in form.cleaned_data.values():
                input.append(item)
            temp = ' '.join([str(elem) for elem in input])
            output = run([sys.executable, '//home//janhavi//django//nnn//Risk_Analysis//web_portal//forms//ML//death_model.py', temp], shell=False, stdout=PIPE)
            messages.success(request, output.stdout)
        else:
            print(form.errors)
            messages.error(request, "Couldn't save your response. Please try again.")
    form = death_form()
    return render(request, 'pages/death.html', {'form':form})

def external(request):
    input = '3'

    output = run([sys.executable, '//home//janhavi//django//nnn//Risk_Analysis//web_portal//forms//ML//transplant_model.py', input], shell=False, stdout=PIPE)
    print(output)

    return render(request, 'pages/external.html', {'data1':output})
