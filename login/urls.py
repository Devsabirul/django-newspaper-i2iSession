from django.urls import path
from .views import *
urlpatterns = [
    path("", signin, name="LOGIN"),
    path('/signup', signup, name="signup"),
    path('/logout', logout_, name="logout_"),
]
