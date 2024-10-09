from django.urls import path

from .import views

app_name = 'users'

urlpatterns = [
    path('signUp/', views.sign_up, name='signup_user'),
    path('login/', views.login, name='login_user')
]