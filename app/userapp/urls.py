from django.urls import path
from userapp.views import LoginView,RegisterView,HomeView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('home/',HomeView.as_view(),name="home"),


]
