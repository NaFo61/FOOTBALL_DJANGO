from django.contrib.auth import views
from django.urls import path

from .views import SignUpView
from .forms import MyLoginForm

app_name = "auth"


urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(
            template_name="auth/login.html",
            form_class=MyLoginForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
    path(
        "signup/",
        SignUpView.as_view(),
        name="signup",
    )
]
