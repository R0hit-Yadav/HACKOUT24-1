from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from .forms import UserRegisterForm, UserProfileForm
from .models import NewsUpdate
from django.urls import reverse


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        return render(request, 'main/profile.html', {'user_profile': user_profile})
    else:
        return redirect('login')

def news_updates(request):
    news = NewsUpdate.objects.all().order_by('-created_at')
    return render(request, 'main/news_updates.html', {'news': news})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'main/register.html', {'form': form, 'profile_form': profile_form})

# views.py

def custom_logout_view(request):
    logout(request)
    return redirect(reverse('home'))  # Redirect to the home page after logout
