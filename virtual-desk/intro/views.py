from django.shortcuts import render


def home(request):
    return render(request, 'intro/home.html', {})


def about(request):
    return render(request, 'intro/about.html', {})


def contact(request):
    return render(request, 'intro/contact.html', {})


def services(request):
    return render(request, 'intro/services.html', {})
