from django.urls import path
from . import views


urlpatterns = [
   path("", views.index, name = "index"),
   path("users_list", views.users_list, name = "users_list"),
   path('login/', views.login_request, name='login'),
   path('register/',views.register_request, name='register'),
   path('logout', views.logout_request, name='logout')
] 
