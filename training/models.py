from django.contrib.auth.models import AbstractUser
from django.db import models


class Atleta(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goal = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["first_name", "last_name", "username"]

    def __str__(self):
        full_name = self.get_full_name()
        return full_name or self.username


class GrupoMuscular(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "grupo muscular"
        verbose_name_plural = "grupos musculares"

    def __str__(self):
        return self.name


class Exercicio(models.Model):
    class Difficulty(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    equipment = models.CharField(max_length=120, blank=True)
    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER,
    )
    muscle_group = models.ForeignKey(
        GrupoMuscular,
        on_delete=models.PROTECT,
        related_name="exercises",
    )
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "exercicio"
        verbose_name_plural = "exercicios"

    def __str__(self):
        return self.name


class FichaDeTreino(models.Model):
    name = models.CharField(max_length=120)
    athlete = models.ForeignKey(
        Atleta,
        on_delete=models.CASCADE,
        related_name="workout_plans",
    )
    objective = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    exercises = models.ManyToManyField(
        Exercicio,
        through="ItemFichaDeTreino",
        related_name="workout_plans",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = "ficha de treino"
        verbose_name_plural = "fichas de treino"

    def __str__(self):
        return f"{self.name} - {self.athlete}"


class ItemFichaDeTreino(models.Model):
    workout_plan = models.ForeignKey(
        FichaDeTreino,
        on_delete=models.CASCADE,
        related_name="items",
    )
    exercise = models.ForeignKey(
        Exercicio,
        on_delete=models.PROTECT,
        related_name="workout_items",
    )
    sets = models.PositiveSmallIntegerField()
    reps = models.CharField(max_length=50)
    load = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rest_seconds = models.PositiveIntegerField(default=60)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["workout_plan", "order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["workout_plan", "order"],
                name="unique_workout_item_order",
            ),
        ]
        verbose_name = "item da ficha de treino"
        verbose_name_plural = "itens da ficha de treino"

    def __str__(self):
        return f"{self.order}. {self.exercise} ({self.workout_plan.name})"
