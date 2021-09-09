from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)

def summarize(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    return None

def account(request):
    return render(request, 'login.html', {})

def library(request):
    return render(request, 'library.html', {})

def studyset(request):
    return render(request, 'studyset.html', {})

def activity(request):
    return render(request, 'activity.html', {})

def login(request):
    if request.method == 'GET':
        context = {'magic_key': 'pk_live_207A0EF93ABE0D60'}
        return render(request, 'login.html', context)
    return None

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {})
    elif request.method == 'POST':
        return None
    return None

def info(request):
    return render(request, 'info.html', {})

def user(request):
    print(request.headers)
    return render(request, 'login.html', {})
