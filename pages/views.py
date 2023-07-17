from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'pages/index.html')


def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        print(username, password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Ana sayfaya yönlendir
        else:
            error_message = "Geçersiz kullanıcı adı veya şifre"

    return render(request, 'pages/login.html', {'error_message': error_message})
