import unittest
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from training.models import (
    Atleta,
    Exercicio,
    FichaDeTreino,
    GrupoMuscular,
    ItemFichaDeTreino,
)


class CoreViewTestData(TestCase):
    def setUp(self):
        self.athlete = Atleta.objects.create_user(
            username="ana",
            password="test-pass",
            first_name="Ana",
            last_name="Costa",
            goal="Condicionamento",
        )
        self.other_athlete = Atleta.objects.create_user(
            username="bruno",
            password="test-pass",
            first_name="Bruno",
            last_name="Lima",
        )
        self.muscle_group = GrupoMuscular.objects.create(
            name="Costas",
            description="Exercicios para dorsais",
            slug="costas",
        )
        self.exercise = Exercicio.objects.create(
            name="Remada baixa",
            description="Remada sentada no cabo",
            equipment="Cabo",
            difficulty=Exercicio.Difficulty.BEGINNER,
            muscle_group=self.muscle_group,
            slug="remada-baixa",
        )
        self.workout_plan = FichaDeTreino.objects.create(
            name="Treino Pull",
            athlete=self.athlete,
            objective="Forca para costas",
            notes="Manter controle na fase excentrica.",
        )
        self.item = ItemFichaDeTreino.objects.create(
            workout_plan=self.workout_plan,
            exercise=self.exercise,
            sets=4,
            reps="10",
            load=Decimal("45.00"),
            rest_seconds=90,
            order=1,
        )


@unittest.skip("Core list views and URLs will be implemented in the CRUD phase.")
class CoreListViewTests(CoreViewTestData):
    def test_muscle_group_list_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:muscle-group-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.muscle_group.name)

    def test_exercise_list_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:exercise-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise.name)

    def test_athlete_list_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:athlete-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.athlete.username)
        self.assertContains(response, self.other_athlete.username)

    def test_workout_plan_list_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:workout-plan-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.workout_plan.name)


@unittest.skip("Core detail views and URLs will be implemented in the CRUD phase.")
class CoreDetailViewTests(CoreViewTestData):
    def test_muscle_group_detail_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(
            reverse("training:muscle-group-detail", kwargs={"slug": self.muscle_group.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.muscle_group.name)
        self.assertContains(response, self.exercise.name)

    def test_exercise_detail_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(
            reverse("training:exercise-detail", kwargs={"slug": self.exercise.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise.name)
        self.assertContains(response, self.muscle_group.name)

    def test_athlete_detail_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(
            reverse("training:athlete-detail", kwargs={"pk": self.athlete.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.athlete.username)

    def test_workout_plan_detail_view(self):
        self.client.force_login(self.athlete)
        response = self.client.get(
            reverse("training:workout-plan-detail", kwargs={"pk": self.workout_plan.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.workout_plan.name)
        self.assertContains(response, self.exercise.name)


@unittest.skip("CRUD views and URLs will be implemented in the CRUD phase.")
class CoreCrudViewTests(CoreViewTestData):
    def test_create_muscle_group(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:muscle-group-create"),
            {"name": "Pernas", "description": "Treino de membros inferiores", "slug": "pernas"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(GrupoMuscular.objects.filter(slug="pernas").exists())

    def test_update_muscle_group(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:muscle-group-update", kwargs={"slug": self.muscle_group.slug}),
            {"name": "Dorsais", "description": "Costas e dorsais", "slug": "dorsais"},
        )

        self.assertEqual(response.status_code, 302)
        self.muscle_group.refresh_from_db()
        self.assertEqual(self.muscle_group.name, "Dorsais")

    def test_delete_muscle_group(self):
        deletable_group = GrupoMuscular.objects.create(name="Abdomen", slug="abdomen")
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:muscle-group-delete", kwargs={"slug": deletable_group.slug})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(GrupoMuscular.objects.filter(pk=deletable_group.pk).exists())

    def test_create_exercise(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:exercise-create"),
            {
                "name": "Puxada alta",
                "description": "Puxada no pulley",
                "equipment": "Pulley",
                "difficulty": Exercicio.Difficulty.BEGINNER,
                "muscle_group": self.muscle_group.pk,
                "slug": "puxada-alta",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Exercicio.objects.filter(slug="puxada-alta").exists())

    def test_update_exercise(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:exercise-update", kwargs={"slug": self.exercise.slug}),
            {
                "name": "Remada baixa aberta",
                "description": self.exercise.description,
                "equipment": self.exercise.equipment,
                "difficulty": Exercicio.Difficulty.INTERMEDIATE,
                "muscle_group": self.muscle_group.pk,
                "slug": self.exercise.slug,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.exercise.refresh_from_db()
        self.assertEqual(self.exercise.name, "Remada baixa aberta")

    def test_delete_exercise(self):
        exercise = Exercicio.objects.create(
            name="Face pull",
            equipment="Cabo",
            difficulty=Exercicio.Difficulty.BEGINNER,
            muscle_group=self.muscle_group,
            slug="face-pull",
        )
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:exercise-delete", kwargs={"slug": exercise.slug})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Exercicio.objects.filter(pk=exercise.pk).exists())

    def test_create_workout_plan(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:workout-plan-create"),
            {
                "name": "Treino Full Body",
                "athlete": self.athlete.pk,
                "objective": "Condicionamento geral",
                "notes": "Treino leve.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(FichaDeTreino.objects.filter(name="Treino Full Body").exists())

    def test_update_workout_plan(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:workout-plan-update", kwargs={"pk": self.workout_plan.pk}),
            {
                "name": "Treino Pull atualizado",
                "athlete": self.athlete.pk,
                "objective": self.workout_plan.objective,
                "notes": self.workout_plan.notes,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.workout_plan.refresh_from_db()
        self.assertEqual(self.workout_plan.name, "Treino Pull atualizado")

    def test_delete_workout_plan(self):
        self.client.force_login(self.athlete)
        response = self.client.post(
            reverse("training:workout-plan-delete", kwargs={"pk": self.workout_plan.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(FichaDeTreino.objects.filter(pk=self.workout_plan.pk).exists())


@unittest.skip("Login-required behavior will be implemented with the CRUD views.")
class AuthenticationRequiredViewTests(CoreViewTestData):
    def test_main_routes_require_login(self):
        protected_routes = [
            reverse("training:muscle-group-list"),
            reverse("training:exercise-list"),
            reverse("training:athlete-list"),
            reverse("training:workout-plan-list"),
            reverse("training:workout-plan-detail", kwargs={"pk": self.workout_plan.pk}),
        ]

        for url in protected_routes:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertIn("/login", response["Location"])


@unittest.skip("Search behavior will be implemented with the list views.")
class SearchViewTests(CoreViewTestData):
    def test_search_exercises_by_name(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:exercise-list"), {"q": "Remada"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise.name)

    def test_search_muscle_groups_by_name(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:muscle-group-list"), {"q": "Costas"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.muscle_group.name)

    def test_search_athletes_by_name_or_username(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:athlete-list"), {"q": "ana"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.athlete.username)

    def test_search_workout_plans_by_name(self):
        self.client.force_login(self.athlete)
        response = self.client.get(reverse("training:workout-plan-list"), {"q": "Pull"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.workout_plan.name)
