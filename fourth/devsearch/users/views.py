from django.shortcuts import render


def profiles(request):
    return render(request, 'users/index.html')

