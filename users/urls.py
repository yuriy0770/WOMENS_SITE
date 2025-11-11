from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('profile/update-user/', views.update_user, name='update_user'),
    path('profile/change-password/', views.change_password, name='change_password'),
]