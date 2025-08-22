from django.urls import path
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_page, name="create"),
    path("search", views.search, name="search"),
    path("edit/<str:title>", views.edit_page, name="edit"),
    path("random", views.random_page, name="random"),
    path("<str:title>", views.entry, name="entry"),
]
