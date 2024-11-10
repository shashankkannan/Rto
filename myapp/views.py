from django.shortcuts import render


def home(request):
    # Add any context or functionality if required
    return render(request, 'home.html')


def pjm(request):
    # Add any context or functionality if required
    return render(request, 'pjm.html')


def nyiso(request):
    # Add any context or functionality if required
    return render(request, 'nyiso.html')


def isone(request):
    # Add any context or functionality if required
    return render(request, 'isone.html')
