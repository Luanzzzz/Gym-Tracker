from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    ExercicioForm,
    FichaDeTreinoForm,
    GrupoMuscularForm,
    ItemFichaDeTreinoForm,
)
from .models import Atleta, Exercicio, FichaDeTreino, GrupoMuscular, ItemFichaDeTreino


class HomeView(TemplateView):
    template_name = "training/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["athlete_count"] = Atleta.objects.count()
        context["muscle_group_count"] = GrupoMuscular.objects.count()
        context["exercise_count"] = Exercicio.objects.count()
        context["workout_plan_count"] = FichaDeTreino.objects.count()
        return context


class SearchQueryMixin:
    search_param = "q"
    search_fields = ()

    def get_search_query(self):
        return self.request.GET.get(self.search_param, "").strip()

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.get_search_query()
        if not query:
            return queryset

        filters = Q()
        for field in self.search_fields:
            filters |= Q(**{f"{field}__icontains": query})
        return queryset.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.get_search_query()
        return context


class AtletaListView(SearchQueryMixin, ListView):
    model = Atleta
    template_name = "training/athlete_list.html"
    context_object_name = "athletes"
    search_fields = ("username", "first_name", "last_name")


class AtletaDetailView(DetailView):
    model = Atleta
    template_name = "training/athlete_detail.html"
    context_object_name = "athlete"


class GrupoMuscularListView(SearchQueryMixin, ListView):
    model = GrupoMuscular
    template_name = "training/muscle_group_list.html"
    context_object_name = "muscle_groups"
    search_fields = ("name",)


class GrupoMuscularDetailView(DetailView):
    model = GrupoMuscular
    template_name = "training/muscle_group_detail.html"
    context_object_name = "muscle_group"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("exercises")


class GrupoMuscularCreateView(CreateView):
    model = GrupoMuscular
    form_class = GrupoMuscularForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Create muscle group", "submit_label": "Create"}


class GrupoMuscularUpdateView(UpdateView):
    model = GrupoMuscular
    form_class = GrupoMuscularForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Edit muscle group", "submit_label": "Save"}


class GrupoMuscularDeleteView(DeleteView):
    model = GrupoMuscular
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Delete muscle group"}


class ExercicioListView(SearchQueryMixin, ListView):
    model = Exercicio
    template_name = "training/exercise_list.html"
    context_object_name = "exercises"
    search_fields = ("name",)

    def get_queryset(self):
        return super().get_queryset().select_related("muscle_group")


class ExercicioDetailView(DetailView):
    model = Exercicio
    template_name = "training/exercise_detail.html"
    context_object_name = "exercise"

    def get_queryset(self):
        return super().get_queryset().select_related("muscle_group")


class ExercicioCreateView(CreateView):
    model = Exercicio
    form_class = ExercicioForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Create exercise", "submit_label": "Create"}


class ExercicioUpdateView(UpdateView):
    model = Exercicio
    form_class = ExercicioForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Edit exercise", "submit_label": "Save"}


class ExercicioDeleteView(DeleteView):
    model = Exercicio
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Delete exercise"}


class FichaDeTreinoListView(SearchQueryMixin, ListView):
    model = FichaDeTreino
    template_name = "training/workout_plan_list.html"
    context_object_name = "workout_plans"
    search_fields = ("name", "objective")

    def get_queryset(self):
        return super().get_queryset().select_related("athlete")


class FichaDeTreinoDetailView(DetailView):
    model = FichaDeTreino
    template_name = "training/workout_plan_detail.html"
    context_object_name = "workout_plan"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("athlete")
            .prefetch_related("items__exercise")
        )


class FichaDeTreinoCreateView(CreateView):
    model = FichaDeTreino
    form_class = FichaDeTreinoForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Create workout plan", "submit_label": "Create"}


class FichaDeTreinoUpdateView(UpdateView):
    model = FichaDeTreino
    form_class = FichaDeTreinoForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Edit workout plan", "submit_label": "Save"}


class FichaDeTreinoDeleteView(DeleteView):
    model = FichaDeTreino
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Delete workout plan"}


class ItemFichaDeTreinoCreateView(CreateView):
    model = ItemFichaDeTreino
    form_class = ItemFichaDeTreinoForm
    template_name = "training/form.html"
    extra_context = {"title": "Create workout item", "submit_label": "Create"}

    def dispatch(self, request, *args, **kwargs):
        self.workout_plan = FichaDeTreino.objects.get(pk=kwargs["workout_plan_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.workout_plan = self.workout_plan
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("training:workout-plan-detail", kwargs={"pk": self.workout_plan.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_plan"] = self.workout_plan
        return context


class ItemFichaDeTreinoUpdateView(UpdateView):
    model = ItemFichaDeTreino
    form_class = ItemFichaDeTreinoForm
    template_name = "training/form.html"
    extra_context = {"title": "Edit workout item", "submit_label": "Save"}

    def get_success_url(self):
        return reverse(
            "training:workout-plan-detail",
            kwargs={"pk": self.object.workout_plan.pk},
        )


class ItemFichaDeTreinoDeleteView(DeleteView):
    model = ItemFichaDeTreino
    template_name = "training/confirm_delete.html"
    extra_context = {"title": "Delete workout item"}

    def get_success_url(self):
        return reverse(
            "training:workout-plan-detail",
            kwargs={"pk": self.object.workout_plan.pk},
        )
