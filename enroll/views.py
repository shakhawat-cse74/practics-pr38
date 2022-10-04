from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('From Valideted')
            print('Name :', fm.cleaned_data['name'])
            print('Email :', fm.cleaned_data['email'])
            print('Password :', fm.cleaned_data['password'])
            print('Repassword :', fm.cleaned_data['repassword'])
    else:
        fm = StudentRegistration()

    return render (request,'enroll/registrationform.html',{'form':fm})