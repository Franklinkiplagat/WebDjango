from django.contrib import messages
from django.shortcuts import render, redirect

from students.forms import StudentForm, NewStudentComplainForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def gallery(request):
    return render(request, 'gallery.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    form = StudentForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    form = NewStudentComplainForm()
    if request.method == 'POST':
        form = NewStudentComplainForm(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        NewStudentComplainForm()
        messages.success(request, 'User Registration Successful')
        return redirect('register')
    else:
        form = NewStudentComplainForm()
    return render(request, 'register.html', {'form': form})
