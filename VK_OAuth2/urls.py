from django.contrib import admin
from django.urls import path, include
from User_Profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.index, name="Login"),
    path('logout/', views.logout_view, name="Logout"),
    path('profile/', views.profile_view, name="Profile"),
    path('', include('social_django.urls', namespace='social')),
]
