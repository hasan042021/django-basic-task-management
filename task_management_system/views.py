from django.shortcuts import render
from tasks.models import Tasks


def home(request):
    all_tasks = Tasks.objects.all()

    return render(request, "home.html", {"data": all_tasks})
