"""This file contains the urls patterns used in the roles app."""
from django.urls import path

from . import views
from django.conf.urls import re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r"^create/?$", views.create_user, name="create"),
    re_path(r"^signin/?$", views.signin_user, name="signin"),
    re_path(r"^profileupdate/?$", views.update_profile, name="profileupdate"),
    re_path(r"^logout/?$", views.logout_user, name="logout"),
    path("like/<int:product_id>/<int:replaced_id>/", views.like, name="like"),
    path("unlike/<int:unliked_id>/", views.unlike, name="unlike"),
    re_path(r"^favourites/?$", views.favourites, name="favourites"),
    re_path(r"^register/?$", views.create_user, name="register"),
    re_path(r"^account/?$", views.update_profile, name="account"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("roles/signin/", views.signin_user, name='login'),
]
