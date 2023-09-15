from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import PasswordOperator, Schedule
from .forms import PasswordForm, ScheduleForm
from .password import generatePassword

from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy, reverse

from plyer import notification
from datetime import datetime

# Create your views here.
class PasswordView(CreateView):
    model = PasswordOperator
    form_class = PasswordForm
    success_url = "schedules"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Edits the context 'form' to be used in html 
        context["passwordForm"] = context["form"]
        return context 


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    success_url = reverse_lazy("schedules")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Edits the context 'form' to be used in html 
        context["scheduleForm"] = context["form"]
        return context
    

def schedulesPageView(request):
    if request.method == 'POST':
        # Checks if the request is a "passLock" request or "schedule" request
        if "password" in request.POST:
            # Assigns data from the request into a variable
            password_data = request.POST
            # Creates and saves a new PasswordOperator object using the data from the request
            new_password_obj = PasswordOperator(
                password = password_data["password"], 
                time = password_data["time"],
                label = password_data["label"],
                )
            new_password_obj.save()
        else:
            schedule_data = request.POST
            new_schedule_obj = Schedule(schedule = schedule_data["schedule"], time = schedule_data["time"])
            new_schedule_obj.save()
        
        # redirects url to "schedules" url (refreshes the page)
        return redirect(reverse("schedules"))
    
    else:
        schedule_response = ScheduleCreateView.as_view()(request)
        password_response = PasswordView.as_view()(request)
        
        context = {}
        context.update(schedule_response.context_data)
        context.update(password_response.context_data)
        context["schedule_objects"] = Schedule.objects.all()
        context["pass_seal_objects"] = PasswordOperator.objects.all()
        return render(request, "schedules.html", context)


# Packs random password in a json response
def randomPasswordView(request):
    random_password = generatePassword()
    pasword_dict = {"random_password": random_password}

    return JsonResponse(pasword_dict)

def currentTimeView(request):
    now = datetime.now()

    # Date
    year_now = now.year
    month_now = now.month
    month_now_str = now.strftime("%B")
    day_now = now.day
    day_now_str = now.strftime("%A")

    # Time
    hour_now = now.hour
    minute_now = now.minute
    second_now = now.second

    time_dict = {
        "now": now,

        # Date 
        "year_now": year_now,
        "month_now": month_now,
        "month_now_str": month_now_str,
        "day_now": day_now,
        "day_now_str": day_now_str,

        # Time
        "hour_now": hour_now,
        "minute_now": minute_now,
        "second_now": second_now,
    }

    return JsonResponse(time_dict)
