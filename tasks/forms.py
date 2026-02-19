from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
            "tags",
            "is_completed",
        )
        widgets = {
            "assignees": forms.CheckboxSelectMultiple,
            "tags": forms.CheckboxSelectMultiple,
            "description": forms.Textarea(attrs={"rows": 4}),
        }
