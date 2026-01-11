from . import views
from django.urls import path

urlpatterns = [
    path("<str:month>", views.monthly_challenge),
]