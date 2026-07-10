# Gym Tracker

Gym Tracker is a Django web application for managing athletes, muscle groups, exercises, and workout plans. It was built as a Mate Academy portfolio project with CRUD flows, authentication, Django templates, Bootstrap UI, tests, and a documented database structure.

## Main Features

- Custom athlete user model based on Django `AbstractUser`.
- Basic authentication with login and logout.
- Dashboard with totals for athletes, muscle groups, exercises, and workout plans.
- CRUD for muscle groups.
- CRUD for exercises.
- CRUD for workout plans.
- CRUD for workout plan items, connecting exercises to a workout plan with sets, reps, load, rest time, and order.
- Search on the main list pages.
- Django admin registration for all core models.
- Bootstrap-based responsive templates.

## Technologies

- Python
- Django 6.0.2
- SQLite for local development
- Django Templates
- Bootstrap 5
- HTML and CSS
- Django test framework

## Main Models

The project has five main models:

- `Atleta`: custom user model that inherits from `AbstractUser`.
- `GrupoMuscular`: muscle group category used to organize exercises.
- `Exercicio`: reusable exercise catalog item linked to a muscle group.
- `FichaDeTreino`: workout plan linked to an athlete.
- `ItemFichaDeTreino`: intermediate model between workout plans and exercises.

Main relationships:

- `Atleta` 1:N `FichaDeTreino`
- `GrupoMuscular` 1:N `Exercicio`
- `FichaDeTreino` N:N `Exercicio` through `ItemFichaDeTreino`

## Database Diagram

The database ER diagram is documented in [docs/database/ER_DIAGRAM.md](docs/database/ER_DIAGRAM.md).

Visual diagram files:

- `docs/database/gym-tracker.drawio`
- `docs/database/gym-tracker-er-diagram..png`

## Running Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Running Tests

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check
```

## Screenshots

No screenshots are currently committed. The UI can be reviewed by running the local server and opening the dashboard, list pages, detail pages, forms, and login page.

## Project Status

Final delivery review stage. The project is ready for Mate Academy activity review and portfolio presentation, with the required models, relationships, CRUD screens, authentication, Bootstrap templates, tests, and ER diagram documentation.

## Learnings

- Creating a custom Django user model with `AbstractUser`.
- Modeling `ForeignKey` and many-to-many relationships with an explicit intermediate model.
- Building class-based CRUD views with reusable forms and templates.
- Protecting app routes with basic authentication.
- Registering related models in Django admin.
- Writing model and view tests for the main behavior.
- Documenting a Django project for PR review and portfolio use.
