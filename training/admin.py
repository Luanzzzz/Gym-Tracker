from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Atleta,
    Exercicio,
    FichaDeTreino,
    GrupoMuscular,
    ItemFichaDeTreino,
)


@admin.register(Atleta)
class AtletaAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Training profile", {"fields": ("birth_date", "height", "weight", "goal")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Training profile", {"fields": ("birth_date", "height", "weight", "goal")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "goal", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name", "goal")


@admin.register(GrupoMuscular)
class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("name", "muscle_group", "equipment", "difficulty")
    list_filter = ("muscle_group", "difficulty")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description", "equipment")


class ItemFichaDeTreinoInline(admin.TabularInline):
    model = ItemFichaDeTreino
    extra = 1


@admin.register(FichaDeTreino)
class FichaDeTreinoAdmin(admin.ModelAdmin):
    inlines = [ItemFichaDeTreinoInline]
    list_display = ("name", "athlete", "objective", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "objective", "athlete__username")


@admin.register(ItemFichaDeTreino)
class ItemFichaDeTreinoAdmin(admin.ModelAdmin):
    list_display = (
        "workout_plan",
        "exercise",
        "order",
        "sets",
        "reps",
        "load",
        "rest_seconds",
    )
    list_filter = ("exercise__muscle_group",)
    search_fields = ("workout_plan__name", "exercise__name")
