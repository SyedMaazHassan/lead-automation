from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .factories import UserFactory, LeadFactory

def home_view(request):
    return redirect("write-with-ai")
    return render(request, 'index.html')

def all_templates(request):
    return render(request, 'template.html')

def create_template(request):
    return render(request, 'create-template.html')

def all_leads(request):
    return render(request, 'leadpage.html')

def single_leads(request):
    return render(request, 'single-lead.html')

def write_with_ai(request):
    return render(request, 'write-with-ai.html')

def register_view(request):
    return render(request, 'register.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
