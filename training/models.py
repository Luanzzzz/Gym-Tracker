from django.contrib.auth.models import AbstractUser
from django.db import models


class Athlete(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goal = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["first_name", "last_name", "username"]

    def __str__(self):
        full_name = self.get_full_name()
        return full_name or self.username


class MuscleGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "muscle group"
        verbose_name_plural = "muscle groups"

    def __str__(self):
        return self.name


class Exercise(models.Model):
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
        MuscleGroup,
        on_delete=models.PROTECT,
        related_name="exercises",
    )
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "exercise"
        verbose_name_plural = "exercises"

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=120)
    athlete = models.ForeignKey(
        Athlete,
        on_delete=models.CASCADE,
        related_name="workout_plans",
    )
    objective = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    exercises = models.ManyToManyField(
        Exercise,
        through="WorkoutItem",
        related_name="workout_plans",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = "workout plan"
        verbose_name_plural = "workout plans"

    def __str__(self):
        return f"{self.name} - {self.athlete}"


class WorkoutItem(models.Model):
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name="items",
    )
    exercise = models.ForeignKey(
        Exercise,
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
        verbose_name = "workout item"
        verbose_name_plural = "workout items"

    def __str__(self):
        return f"{self.order}. {self.exercise} ({self.workout_plan.name})"
