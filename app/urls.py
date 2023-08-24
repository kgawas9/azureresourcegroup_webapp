from django.urls import path

from . import views

urlpatterns = [
    path('', views.read_resource_groups, name='read-resource-groups'),
]
