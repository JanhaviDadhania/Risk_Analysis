#Following Features are to be taken as input from user to predict death label:-

# 'Gender',
# 'Age',
# 'Weight',
# 'BMI',
# 'Systolic Pressure',
# 'Diastolic Pressure',
# 'Total Cholesterol',
# 'HDL',
# 'LDL',
# 'Total Cholesterol/HDL',
# 'Triglycerides',
# 'Platelets',
# 'Lymphocytes',
# 'Neutrophils',
# 'Monocytes',
# 'Eosinophils',
# 'Basophils',
# 'Glycemia',
# 'Total Bilirubin',
# 'Albumin',
# 'Creatinine',
# 'Natremia',
# 'INR',
# 'Smoking',
# 'Diabetes PreTx',
# 'HyperTension',
# 'Functional Study of Positive Ischemia',
# 'Hepatocellular Carcinoma',
# 'Aspirin',
# 'Statins',
# 'Prednisone',
# 'Tacrolimus',
# 'Ciclosoporine',
# 'Azathioprine',
# 'Contraindication for TH',
# 'Entry List',
# 'MELD Score',
# 'Framingham CV Risk',
# 'Vascular Age',
# 'Vascular Age - Biological Age'

from pickle import load
import numpy as np
import sys

# death_scaler = load(open('Death_scaler.pkl', 'rb'))
death_scaler = load(open('/home/janhavi/django/nnn/Risk_Analysis/web_portal/forms/ML/Death_scaler.pkl', 'rb'))
# death_clf = load(open('Death_model.pkl', 'rb'))
death_clf = load(open('/home/janhavi/django/nnn/Risk_Analysis/web_portal/forms/ML/Death_model.pkl', 'rb'))
X = sys.argv[1]
# X = list(map(float, X.split()))
#print(X)
Y = []
X = list(X.split())
for item in X :
    if item == "Male":
        Y.append(0)
    elif item == "Female":
        Y.append(1)
    else :
        Y.append(float(item))
X = Y
print(X)
final = []
final.append(X)

#To demonstrate functionality we are using 40 zeros, instead actual features should be stored in X in the same order as mentioned above which are taken as input from user
X = np.zeros((1,40))
X = final
X = death_scaler.transform(X)

death_label = death_clf.predict(X)
print("Death Label is :- " + str(int(death_label)))
