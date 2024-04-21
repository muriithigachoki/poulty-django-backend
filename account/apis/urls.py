from django.urls import path
from account.apis.views import SignUpAPI, SignInAPI, UsersApiView, UsersDetailsApiView
from knox import views as knox_views

urlpatterns = [
    path("register/", SignUpAPI.as_view()),
    path("login/", SignInAPI.as_view()),
    path("users/", UsersApiView.as_view()),
    path("users/<int:pk>/", UsersDetailsApiView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox-logout"),
]
