from django.urls import path

from . import views

app_name = "training"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("athletes/", views.AtletaListView.as_view(), name="athlete-list"),
    path("athletes/<int:pk>/", views.AtletaDetailView.as_view(), name="athlete-detail"),
    path(
        "muscle-groups/",
        views.GrupoMuscularListView.as_view(),
        name="muscle-group-list",
    ),
    path(
        "muscle-groups/<int:pk>/",
        views.GrupoMuscularDetailView.as_view(),
        name="muscle-group-detail",
    ),
    path(
        "muscle-groups/create/",
        views.GrupoMuscularCreateView.as_view(),
        name="muscle-group-create",
    ),
    path(
        "muscle-groups/<int:pk>/edit/",
        views.GrupoMuscularUpdateView.as_view(),
        name="muscle-group-update",
    ),
    path(
        "muscle-groups/<int:pk>/delete/",
        views.GrupoMuscularDeleteView.as_view(),
        name="muscle-group-delete",
    ),
    path("exercises/", views.ExercicioListView.as_view(), name="exercise-list"),
    path(
        "exercises/<int:pk>/",
        views.ExercicioDetailView.as_view(),
        name="exercise-detail",
    ),
    path("exercises/create/", views.ExercicioCreateView.as_view(), name="exercise-create"),
    path(
        "exercises/<int:pk>/edit/",
        views.ExercicioUpdateView.as_view(),
        name="exercise-update",
    ),
    path(
        "exercises/<int:pk>/delete/",
        views.ExercicioDeleteView.as_view(),
        name="exercise-delete",
    ),
    path(
        "workout-plans/",
        views.FichaDeTreinoListView.as_view(),
        name="workout-plan-list",
    ),
    path(
        "workout-plans/<int:pk>/",
        views.FichaDeTreinoDetailView.as_view(),
        name="workout-plan-detail",
    ),
    path(
        "workout-plans/create/",
        views.FichaDeTreinoCreateView.as_view(),
        name="workout-plan-create",
    ),
    path(
        "workout-plans/<int:pk>/edit/",
        views.FichaDeTreinoUpdateView.as_view(),
        name="workout-plan-update",
    ),
    path(
        "workout-plans/<int:pk>/delete/",
        views.FichaDeTreinoDeleteView.as_view(),
        name="workout-plan-delete",
    ),
    path(
        "workout-plans/<int:workout_plan_pk>/items/create/",
        views.ItemFichaDeTreinoCreateView.as_view(),
        name="workout-item-create",
    ),
    path(
        "workout-items/<int:pk>/edit/",
        views.ItemFichaDeTreinoUpdateView.as_view(),
        name="workout-item-update",
    ),
    path(
        "workout-items/<int:pk>/delete/",
        views.ItemFichaDeTreinoDeleteView.as_view(),
        name="workout-item-delete",
    ),
]
