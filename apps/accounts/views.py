"""
Views for authentication and profile management.
"""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import LoginForm
from .forms import ProfileForm
from .forms import RegisterForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard:home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration successful.",
            )

            return redirect(
                "dashboard:home"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard:home")

    form = LoginForm(
        request,
        data=request.POST or None,
    )

    if request.method == "POST":

        if form.is_valid():

            login(
                request,
                form.get_user(),
            )

            messages.success(
                request,
                "Login successful.",
            )

            return redirect(
                "dashboard:home"
            )

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully.",
    )

    return redirect(
        "accounts:login"
    )


@login_required
def profile_view(request):

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully.",
            )

            return redirect(
                "accounts:profile"
            )

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/profile.html",
        {"form": form},
    )