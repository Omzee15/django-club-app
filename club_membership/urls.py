from django.contrib import admin
from django.urls import path, include
from members import views as member_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member_views.user_login, name='home'),
    path('login/', member_views.user_login, name='login'),
    path('logout/', member_views.user_logout, name='logout'),
    path('dashboard/', member_views.dashboard, name='dashboard'),
    path('profile/', member_views.profile, name='profile'),
    path('register/', member_views.register, name='register'),
    path('members/', include('members.urls')),
    path('activities/', include('activities.urls')),
]