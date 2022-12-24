from django.urls import path

from . import views

app_name = "logistics"
urlpatterns = [
    path("track/", views.OrderTrack.as_view(), name="track"),
]
