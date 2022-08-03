from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('profile/<str:username>', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.user_registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
]
