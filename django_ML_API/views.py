from django.shortcuts import render


def home(request):
    return render(request, "Formation.html")


def about(request):
    return render(request, "about.html")
