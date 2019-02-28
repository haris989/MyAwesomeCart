from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/", views.blogpost, name="blogHome")
]
