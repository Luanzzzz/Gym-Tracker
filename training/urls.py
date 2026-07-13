from django.urls import path

from . import views

app_name = "training"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("athletes/", views.AthleteListView.as_view(), name="athlete-list"),
    path("athletes/<int:pk>/", views.AthleteDetailView.as_view(), name="athlete-detail"),
    path(
        "muscle-groups/",
        views.MuscleGroupListView.as_view(),
        name="muscle-group-list",
    ),
    path(
        "muscle-groups/<int:pk>/",
        views.MuscleGroupDetailView.as_view(),
        name="muscle-group-detail",
    ),
    path(
        "muscle-groups/create/",
        views.MuscleGroupCreateView.as_view(),
        name="muscle-group-create",
    ),
    path(
        "muscle-groups/<int:pk>/edit/",
        views.MuscleGroupUpdateView.as_view(),
        name="muscle-group-update",
    ),
    path(
        "muscle-groups/<int:pk>/delete/",
        views.MuscleGroupDeleteView.as_view(),
        name="muscle-group-delete",
    ),
    path("exercises/", views.ExerciseListView.as_view(), name="exercise-list"),
    path(
        "exercises/<int:pk>/",
        views.ExerciseDetailView.as_view(),
        name="exercise-detail",
    ),
    path("exercises/create/", views.ExerciseCreateView.as_view(), name="exercise-create"),
    path(
        "exercises/<int:pk>/edit/",
        views.ExerciseUpdateView.as_view(),
        name="exercise-update",
    ),
    path(
        "exercises/<int:pk>/delete/",
        views.ExerciseDeleteView.as_view(),
        name="exercise-delete",
    ),
    path(
        "workout-plans/",
        views.WorkoutPlanListView.as_view(),
        name="workout-plan-list",
    ),
    path(
        "workout-plans/<int:pk>/",
        views.WorkoutPlanDetailView.as_view(),
        name="workout-plan-detail",
    ),
    path(
        "workout-plans/create/",
        views.WorkoutPlanCreateView.as_view(),
        name="workout-plan-create",
    ),
    path(
        "workout-plans/<int:pk>/edit/",
        views.WorkoutPlanUpdateView.as_view(),
        name="workout-plan-update",
    ),
    path(
        "workout-plans/<int:pk>/delete/",
        views.WorkoutPlanDeleteView.as_view(),
        name="workout-plan-delete",
    ),
    path(
        "workout-plans/<int:workout_plan_pk>/items/create/",
        views.WorkoutItemCreateView.as_view(),
        name="workout-item-create",
    ),
    path(
        "workout-items/<int:pk>/edit/",
        views.WorkoutItemUpdateView.as_view(),
        name="workout-item-update",
    ),
    path(
        "workout-items/<int:pk>/delete/",
        views.WorkoutItemDeleteView.as_view(),
        name="workout-item-delete",
    ),
]
