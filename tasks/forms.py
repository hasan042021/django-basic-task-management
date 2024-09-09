from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": "5"}),
            "categories": forms.CheckboxSelectMultiple(),
        }
