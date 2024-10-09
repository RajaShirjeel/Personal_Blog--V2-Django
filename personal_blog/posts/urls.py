from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('new_post', views.create_form, name='create_form')
]