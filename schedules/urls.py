from django.urls import path

from .views import randomPasswordView, schedulesPageView, currentTimeView

urlpatterns = [
    path("", schedulesPageView, name="schedules"),
    path("schedules.random_password/", randomPasswordView, name="random_password"),
    path("schedules.time_now/", currentTimeView, name="time_now"),
]
