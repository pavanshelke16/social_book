from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from social_book_app.models import CustomUser
from .models import UploadedFile
from .forms import UploadedFileForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})
    return render(request, 'register.html')

def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'authors_and_sellers.html', {'users': users})

def dummy(request):
    return render(request, 'dummy.html')



def upload_books(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html', {'name': request.user.first_name})
    else:
        form = UploadedFileForm(user=request.user)

    return render(request, 'upload_books.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def uploaded_books(request):
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_books.html', {'uploaded_files': uploaded_files})
