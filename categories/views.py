from django.shortcuts import render, redirect
from .forms import CategoryForm


# Create your views here.
def add_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("add_category")
    else:
        category_form = CategoryForm()

    return render(request, "categories.html", {"form": category_form})


def edit_category(request, id):
    return "edited"


def delete_category(request, id):
    return "deleted"
