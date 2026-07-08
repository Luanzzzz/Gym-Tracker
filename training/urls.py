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
    path("exercises/", views.ExercicioListView.as_view(), name="exercise-list"),
    path(
        "exercises/<int:pk>/",
        views.ExercicioDetailView.as_view(),
        name="exercise-detail",
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
]
