from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from members.models import Membership
from .models import Activity, Enrollment

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activities/activity_list.html', {'activities': activities})

@login_required
def enroll(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    
    # Check if user has a membership
    try:
        membership = Membership.objects.get(user=request.user)
    except Membership.DoesNotExist:
        messages.error(request, "You need to be a member to enroll in activities")
        return redirect('dashboard')
    
    # Check if already enrolled
    if activity.members.filter(id=membership.id).exists():
        messages.info(request, "You are already enrolled in this activity")
    else:
        activity.members.add(membership)
        messages.success(request, f"Successfully enrolled in {activity.name}")
    
    return redirect('dashboard')

@login_required
def dashboard(request):
    user_membership = Membership.objects.filter(user=request.user).first()
    
    if user_membership:
        enrolled_activities = Activity.objects.filter(members=user_membership)
    else:
        enrolled_activities = []

    context = {
        'user_membership': user_membership,
        'enrolled_activities': enrolled_activities,
    }
    return render(request, 'members/dashboard.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout