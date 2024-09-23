from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import User
# Create your views here.
def index(request):
    return render(request, "thrift/index.html")

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return render(request, template_name = "thrift/index.html")
    else:
        form = SignUpForm()
    return render(request, 'thrift/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request = request, template_name = "thrift/purpose.html")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "thrift/login.html", context={"form":form})

def purpose(request):
    return render(request, "thrift/purpose.html")

# Create your views here.
def upload_item(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ItemForm()
    return render(request, 'uploadItem.html', {'form' : form})


def success(request):
    return HttpResponse('successfully uploaded')
