from django.urls import path
from . import views

app_name = "expense"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:id>/", views.edit, name="edit"),
]