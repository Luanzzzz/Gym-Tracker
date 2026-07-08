from django.db.models import Q
from django.views.generic import DetailView, ListView, TemplateView

from .models import Atleta, Exercicio, FichaDeTreino, GrupoMuscular


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
