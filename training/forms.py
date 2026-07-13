from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Exercise, MuscleGroup, WorkoutItem, WorkoutPlan


def apply_bootstrap_classes(fields):
    for field in fields.values():
        widget = field.widget
        if isinstance(widget, forms.CheckboxInput):
            widget.attrs.setdefault("class", "form-check-input")
        elif isinstance(widget, forms.Select):
            widget.attrs.setdefault("class", "form-select")
        else:
            widget.attrs.setdefault("class", "form-control")


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_classes(self.fields)


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_classes(self.fields)


class MuscleGroupForm(BootstrapModelForm):
    class Meta:
        model = MuscleGroup
        fields = ["name", "description", "slug"]


class ExerciseForm(BootstrapModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "description", "equipment", "difficulty", "muscle_group", "slug"]


class WorkoutPlanForm(BootstrapModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ["name", "athlete", "objective", "notes"]


class WorkoutItemForm(BootstrapModelForm):
    class Meta:
        model = WorkoutItem
        fields = ["exercise", "sets", "reps", "load", "rest_seconds", "order"]
