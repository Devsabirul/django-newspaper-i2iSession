from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HOME"),
    path('news', news, name="news"),
    path('news/singlenews/<slug:slug>', singlenews, name="singlenews"),
]
