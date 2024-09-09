from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Tasks


# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")

    else:
        task_form = TaskForm()
    return render(request, "tasks.html", {"form": task_form})


def edit_task(request, id):
    task_to_edit = Tasks.objects.get(pk=id)
    task_form = TaskForm(instance=task_to_edit)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task_to_edit)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
    return render(request, "tasks.html", {"form": task_form})


def delete_task(request, id):
    task_to_delete = Tasks.objects.get(pk=id)
    task_to_delete.delete()
    return redirect("homepage")
