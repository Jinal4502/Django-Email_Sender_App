from django.shortcuts import render, redirect
from email_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from .forms import SignupForm
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            receipent = request.POST['receipent']
            receipent_list = [receipent,]
            username = request.POST['username']
            message = f"Hello {username}, thanks for joining us. This is an automated message."
            subject = "Welcome to Jinal and Company!"
            send_mail(subject, message, EMAIL_HOST_USER, receipent_list, fail_silently=False)
            return render(request, 'success.html')
        else:
            error = True
            mydic = {
                "form": form(),
                "error": error
            }
            return render(request, 'signup.html', context=mydic)
    mydic = {
        "form": SignupForm()
    }
    return render(request, 'signup.html', context=mydic)

def about(request):
    return render(request, 'dashboard.html')

# def signup(request):
#     sub = forms.Subscribe()
#     if request.method == "POST":
#         sub = forms.Subscribe(request.POST)
#         subject = "Welcome to Jinal Vyas and Company!"
#         message = 'Hope you are enjoying your Django Tutorials'
#         receipent = str(sub['Email'].value())
#         send_mail(subject, message, EMAIL_HOST_USER, [receipent], fail_silently=False)
#         return render(request, 'success.html', {'receipent': receipent})
#     return render(request, 'dashboard.html', {'form': sub})
