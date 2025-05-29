from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Membership, Activity

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'members/login.html', {'error': 'Invalid credentials'})
    return render(request, 'members/login.html')

@login_required
def dashboard(request):
    try:
        membership = Membership.objects.get(user=request.user)
        activities = Activity.objects.filter(members=membership)
        membership_status = True
    except Membership.DoesNotExist:
        activities = []
        membership_status = False
    
    context = {
        'activities': activities,
        'membership_status': membership_status
    }
    return render(request, 'members/dashboard.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    try:
        membership = Membership.objects.get(user=request.user)
        activities = Activity.objects.filter(members=membership)
    except Membership.DoesNotExist:
        membership = None
        activities = []
    
    context = {
        'membership': membership,
        'activities': activities
    }
    return render(request, 'members/profile.html', context)

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if user already exists
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken. Please choose another username.")
            return render(request, 'members/register.html')
        
        try:
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Create membership
            Membership.objects.create(user=user, is_member=True)
            
            # Login the user
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the club.")
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {str(e)}")
            return render(request, 'members/register.html')
    
    return render(request, 'members/register.html')