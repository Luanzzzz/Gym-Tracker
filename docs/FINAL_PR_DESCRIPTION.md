# Final PR Description

Suggested title:

```text
Chore: prepare Gym Tracker portfolio delivery
```

Suggested description:

```md
## Summary
- Finalize Gym Tracker documentation for Mate Academy review and portfolio use.
- Document the database model, ER diagram, implemented CRUD flows, authentication, Bootstrap templates, and test coverage.
- Align project docs with the current Django implementation.

## Requirements coverage
- [x] Project has 4+ models: `Atleta`, `GrupoMuscular`, `Exercicio`, `FichaDeTreino`, and `ItemFichaDeTreino`.
- [x] `Atleta` inherits from Django `AbstractUser`.
- [x] Database includes `ForeignKey` relationships.
- [x] Database includes a many-to-many relationship between `FichaDeTreino` and `Exercicio` through `ItemFichaDeTreino`.
- [x] ER diagram is included in `docs/database/ER_DIAGRAM.md`.
- [x] CRUD is implemented for muscle groups, exercises, workout plans, and workout plan items.
- [x] Basic authentication is configured with login, logout, and protected routes.
- [x] Bootstrap is used in the templates and forms.
- [x] Model and view tests are included.

## How to test
- `python manage.py check`
- `python manage.py test`
- `python manage.py makemigrations --check`

## Notes
- Advanced permissions are intentionally out of scope.
- The project keeps the same expected complexity as the Mate Academy Taxi Service activity without copying its theme.
```
