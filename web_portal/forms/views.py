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
            list_input = []
            print(list_input.append(form.cleaned_data['Gender']))
            print(list_input.append(form.cleaned_data['Age']))
            print(list_input.append(form.cleaned_data['Weight']))
            print(list_input.append(form.cleaned_data['BMI']))
            print(list_input.append(form.cleaned_data['Systolic_Pressure']))
            print(list_input.append(form.cleaned_data['Diastolic_Pressure']))
            print(list_input.append(form.cleaned_data['Total_Cholesterol']))
            print(list_input.append(form.cleaned_data['HDL']))
            print(list_input.append(form.cleaned_data['LDL']))
            print(list_input.append(form.cleaned_data['Total_Cholesterol_HDL']))
            print(list_input.append(form.cleaned_data['Triglycerides']))
            print(list_input.append(form.cleaned_data['Platelets']))
            print(list_input.append(form.cleaned_data['Lymphocytes']))
            print(list_input.append(form.cleaned_data['Neutrophils']))
            print(list_input.append(form.cleaned_data['Monocytes']))
            print(list_input.append(form.cleaned_data['Eosinophils']))
            print(list_input.append(form.cleaned_data['Basophils']))
            print(list_input.append(form.cleaned_data['Glycemia']))
            print(list_input.append(form.cleaned_data['Total_Bilirubin']))
            print(list_input.append(form.cleaned_data['Albumin']))
            print(list_input.append(form.cleaned_data['Creatinine']))
            print(list_input.append(form.cleaned_data['Natremia']))
            print(list_input.append(form.cleaned_data['INR']))
            print(list_input.append(form.cleaned_data['Smoking']))
            print(list_input.append(form.cleaned_data['Diabetes_PreTx']))
            print(list_input.append(form.cleaned_data['HyperTension']))
            print(list_input.append(form.cleaned_data['Functional_Study_of_Positive_Ischemia']))
            print(list_input.append(form.cleaned_data['Hepatocellular_Carcinoma']))
            print(list_input.append(form.cleaned_data['Aspirin']))
            print(list_input.append(form.cleaned_data['Statins']))
            print(list_input.append(form.cleaned_data['Prednisone']))
            print(list_input.append(form.cleaned_data['Tacrolimus']))
            print(list_input.append(form.cleaned_data['Ciclosoporine']))
            print(list_input.append(form.cleaned_data['Azathioprine']))
            print(list_input.append(form.cleaned_data['Contraindication_for_TH']))
            print(list_input.append(form.cleaned_data['Entry_List']))
            print(list_input.append(form.cleaned_data['MELD_Score']))
            print(list_input.append(form.cleaned_data['Framingham_CV_Risk']))
            print(list_input.append(form.cleaned_data['Vascular_Age']))
            print(list_input.append(form.cleaned_data['Vascular_Age_Biological_Age']))
            temp = ' '.join([str(elem) for elem in list_input])
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
            list_input = []
            print(list_input.append(form.cleaned_data['Gender']))
            print(list_input.append(form.cleaned_data['Age']))
            print(list_input.append(form.cleaned_data['Weight']))
            print(list_input.append(form.cleaned_data['BMI']))
            print(list_input.append(form.cleaned_data['Systolic_Pressure']))
            print(list_input.append(form.cleaned_data['Diastolic_Pressure']))
            print(list_input.append(form.cleaned_data['Total_Cholesterol']))
            print(list_input.append(form.cleaned_data['HDL']))
            print(list_input.append(form.cleaned_data['LDL']))
            print(list_input.append(form.cleaned_data['Total_Cholesterol_HDL']))
            print(list_input.append(form.cleaned_data['Triglycerides']))
            print(list_input.append(form.cleaned_data['Platelets']))
            print(list_input.append(form.cleaned_data['Lymphocytes']))
            print(list_input.append(form.cleaned_data['Neutrophils']))
            print(list_input.append(form.cleaned_data['Monocytes']))
            print(list_input.append(form.cleaned_data['Eosinophils']))
            print(list_input.append(form.cleaned_data['Basophils']))
            print(list_input.append(form.cleaned_data['Glycemia']))
            print(list_input.append(form.cleaned_data['Total_Bilirubin']))
            print(list_input.append(form.cleaned_data['Albumin']))
            print(list_input.append(form.cleaned_data['Creatinine']))
            print(list_input.append(form.cleaned_data['Natremia']))
            print(list_input.append(form.cleaned_data['INR']))
            print(list_input.append(form.cleaned_data['Smoking']))
            print(list_input.append(form.cleaned_data['Diabetes_PreTx']))
            print(list_input.append(form.cleaned_data['HyperTension']))
            print(list_input.append(form.cleaned_data['Functional_Study_of_Positive_Ischemia']))
            print(list_input.append(form.cleaned_data['Hepatocellular_Carcinoma']))
            print(list_input.append(form.cleaned_data['Aspirin']))
            print(list_input.append(form.cleaned_data['Statins']))
            print(list_input.append(form.cleaned_data['Prednisone']))
            print(list_input.append(form.cleaned_data['Tacrolimus']))
            print(list_input.append(form.cleaned_data['Ciclosoporine']))
            print(list_input.append(form.cleaned_data['Azathioprine']))
            print(list_input.append(form.cleaned_data['Contraindication_for_TH']))
            print(list_input.append(form.cleaned_data['Entry_List']))
            print(list_input.append(form.cleaned_data['MELD_Score']))
            print(list_input.append(form.cleaned_data['Framingham_CV_Risk']))
            print(list_input.append(form.cleaned_data['Vascular_Age']))
            print(list_input.append(form.cleaned_data['Vascular_Age_Biological_Age']))
            temp = ' '.join([str(elem) for elem in list_input])
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
