from django import forms

from .models import Exercicio, FichaDeTreino, GrupoMuscular, ItemFichaDeTreino


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "form-check-input")
            else:
                widget.attrs.setdefault("class", "form-control")


class GrupoMuscularForm(BootstrapModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ["name", "description", "slug"]


class ExercicioForm(BootstrapModelForm):
    class Meta:
        model = Exercicio
        fields = ["name", "description", "equipment", "difficulty", "muscle_group", "slug"]


class FichaDeTreinoForm(BootstrapModelForm):
    class Meta:
        model = FichaDeTreino
        fields = ["name", "athlete", "objective", "notes"]


class ItemFichaDeTreinoForm(BootstrapModelForm):
    class Meta:
        model = ItemFichaDeTreino
        fields = ["exercise", "sets", "reps", "load", "rest_seconds", "order"]
