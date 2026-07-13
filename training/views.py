from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
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
    ExerciseForm,
    MuscleGroupForm,
    WorkoutItemForm,
    WorkoutPlanForm,
)
from .models import Athlete, Exercise, MuscleGroup, WorkoutItem, WorkoutPlan


class HomeView(TemplateView):
    template_name = "training/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["athlete_count"] = Athlete.objects.count()
        context["muscle_group_count"] = MuscleGroup.objects.count()
        context["exercise_count"] = Exercise.objects.count()
        context["workout_plan_count"] = WorkoutPlan.objects.count()
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


class AthleteListView(LoginRequiredMixin, SearchQueryMixin, ListView):
    model = Athlete
    template_name = "training/athlete_list.html"
    context_object_name = "athletes"
    search_fields = ("username", "first_name", "last_name")


class AthleteDetailView(LoginRequiredMixin, DetailView):
    model = Athlete
    template_name = "training/athlete_detail.html"
    context_object_name = "athlete"


class MuscleGroupListView(LoginRequiredMixin, SearchQueryMixin, ListView):
    model = MuscleGroup
    template_name = "training/muscle_group_list.html"
    context_object_name = "muscle_groups"
    search_fields = ("name",)


class MuscleGroupDetailView(LoginRequiredMixin, DetailView):
    model = MuscleGroup
    template_name = "training/muscle_group_detail.html"
    context_object_name = "muscle_group"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("exercises")


class MuscleGroupCreateView(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = MuscleGroupForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Create muscle group", "submit_label": "Create"}


class MuscleGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = MuscleGroup
    form_class = MuscleGroupForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Edit muscle group", "submit_label": "Save"}


class MuscleGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = MuscleGroup
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:muscle-group-list")
    extra_context = {"title": "Delete muscle group"}


class ExerciseListView(LoginRequiredMixin, SearchQueryMixin, ListView):
    model = Exercise
    template_name = "training/exercise_list.html"
    context_object_name = "exercises"
    search_fields = ("name",)

    def get_queryset(self):
        return super().get_queryset().select_related("muscle_group")


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = "training/exercise_detail.html"
    context_object_name = "exercise"

    def get_queryset(self):
        return super().get_queryset().select_related("muscle_group")


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Create exercise", "submit_label": "Create"}


class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Edit exercise", "submit_label": "Save"}


class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:exercise-list")
    extra_context = {"title": "Delete exercise"}


class WorkoutPlanListView(LoginRequiredMixin, SearchQueryMixin, ListView):
    model = WorkoutPlan
    template_name = "training/workout_plan_list.html"
    context_object_name = "workout_plans"
    search_fields = ("name", "objective")

    def get_queryset(self):
        return super().get_queryset().select_related("athlete")


class WorkoutPlanDetailView(LoginRequiredMixin, DetailView):
    model = WorkoutPlan
    template_name = "training/workout_plan_detail.html"
    context_object_name = "workout_plan"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("athlete")
            .prefetch_related("items__exercise")
        )


class WorkoutPlanCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Create workout plan", "submit_label": "Create"}


class WorkoutPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    template_name = "training/form.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Edit workout plan", "submit_label": "Save"}


class WorkoutPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkoutPlan
    template_name = "training/confirm_delete.html"
    success_url = reverse_lazy("training:workout-plan-list")
    extra_context = {"title": "Delete workout plan"}


class WorkoutItemCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutItem
    form_class = WorkoutItemForm
    template_name = "training/form.html"
    extra_context = {"title": "Create workout item", "submit_label": "Create"}

    def dispatch(self, request, *args, **kwargs):
        self.workout_plan = WorkoutPlan.objects.get(pk=kwargs["workout_plan_pk"])
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


class WorkoutItemUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkoutItem
    form_class = WorkoutItemForm
    template_name = "training/form.html"
    extra_context = {"title": "Edit workout item", "submit_label": "Save"}

    def get_success_url(self):
        return reverse(
            "training:workout-plan-detail",
            kwargs={"pk": self.object.workout_plan.pk},
        )


class WorkoutItemDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkoutItem
    template_name = "training/confirm_delete.html"
    extra_context = {"title": "Delete workout item"}

    def get_success_url(self):
        return reverse(
            "training:workout-plan-detail",
            kwargs={"pk": self.object.workout_plan.pk},
        )
