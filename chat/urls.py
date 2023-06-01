from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.empty_chat, name = "empty_chat"),
    path("<int:id>/", views.chat, name = "chat")
]