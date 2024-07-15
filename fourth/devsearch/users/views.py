from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout


def login_user(request):
    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def profiles(request):
    prof = Profile.objects.all()
    context = {"profiles": prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")  # exact - точное совпадение
    other_skills = prof.skill_set.filter(description="")

    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'users/profile.html', context)

