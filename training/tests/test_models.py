from decimal import Decimal

from django.test import TestCase

from training.models import (
    Athlete,
    Exercise,
    MuscleGroup,
    WorkoutItem,
    WorkoutPlan,
)


class TrainingModelTests(TestCase):
    def setUp(self):
        self.athlete = Athlete.objects.create_user(
            username="mateus",
            password="test-pass",
            first_name="Mateus",
            last_name="Silva",
            goal="Hipertrofia",
            height=Decimal("1.80"),
            weight=Decimal("82.50"),
        )
        self.muscle_group = MuscleGroup.objects.create(
            name="Peito",
            description="Exercicios para peitoral",
            slug="peito",
        )
        self.exercise = Exercise.objects.create(
            name="Supino reto",
            description="Exercicio com barra para peitoral",
            equipment="Barra",
            difficulty=Exercise.Difficulty.INTERMEDIATE,
            muscle_group=self.muscle_group,
            slug="supino-reto",
        )
        self.workout_plan = WorkoutPlan.objects.create(
            name="Treino A",
            athlete=self.athlete,
            objective="Forca e hipertrofia",
            notes="Priorizar tecnica antes de aumentar carga.",
        )

    def test_model_str_methods(self):
        item = WorkoutItem.objects.create(
            workout_plan=self.workout_plan,
            exercise=self.exercise,
            sets=4,
            reps="8-10",
            load=Decimal("60.00"),
            rest_seconds=90,
            order=1,
        )

        self.assertEqual(str(self.athlete), "Mateus Silva")
        self.assertEqual(str(self.muscle_group), "Peito")
        self.assertEqual(str(self.exercise), "Supino reto")
        self.assertEqual(str(self.workout_plan), "Treino A - Mateus Silva")
        self.assertEqual(str(item), "1. Supino reto (Treino A)")

    def test_foreign_key_relationships(self):
        self.assertEqual(self.exercise.muscle_group, self.muscle_group)
        self.assertEqual(self.workout_plan.athlete, self.athlete)
        self.assertIn(self.exercise, self.muscle_group.exercises.all())
        self.assertIn(self.workout_plan, self.athlete.workout_plans.all())

    def test_workout_plan_with_intermediate_item(self):
        item = WorkoutItem.objects.create(
            workout_plan=self.workout_plan,
            exercise=self.exercise,
            sets=3,
            reps="12",
            load=Decimal("50.00"),
            rest_seconds=60,
            order=1,
        )

        self.assertEqual(item.workout_plan, self.workout_plan)
        self.assertEqual(item.exercise, self.exercise)
        self.assertEqual(self.workout_plan.items.count(), 1)
        self.assertEqual(self.exercise.workout_items.count(), 1)
        self.assertIn(self.exercise, self.workout_plan.exercises.all())
        self.assertIn(self.workout_plan, self.exercise.workout_plans.all())
