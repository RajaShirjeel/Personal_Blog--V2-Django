from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('create_comment/<slug:slug>', view=views.create_comment, name='create_comment'),
    path('delete_comment/<int:pk>/<slug:slug>', views.delete_comment, name='delete_comment')
]