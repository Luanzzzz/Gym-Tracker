# Gym Tracker

Gym Tracker sera uma aplicacao Django para gerenciar atletas, grupos musculares, exercicios e fichas de treino.

Este arquivo e um rascunho inicial do README. Ele deve ser atualizado conforme o projeto Django for implementado.

## Descricao

O sistema tera como foco o gerenciamento de fichas de treino para academia. Um atleta podera ter fichas de treino, e cada ficha sera composta por exercicios organizados por ordem, series, repeticoes, carga, descanso e observacoes.

O projeto sera desenvolvido como portfolio para a Mate Academy, demonstrando uso de Django, autenticacao, models, relacionamentos, templates e Bootstrap.

## Tecnologias previstas

- Python
- Django
- SQLite em desenvolvimento
- HTML
- CSS
- Bootstrap ou template pronto compativel com Django
- Django Templates
- Git e GitHub

## Como rodar localmente

As instrucoes abaixo representam o fluxo previsto. Os comandos devem ser revisados depois que o projeto Django for criado.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois disso, a aplicacao devera ficar disponivel em:

```text
http://127.0.0.1:8000/
```

## Estrutura prevista

Estrutura esperada depois da criacao do projeto Django:

```text
Gym-Tracker/
├── docs/
│   ├── PROJECT_SPEC.md
│   ├── DATABASE_MODEL.md
│   ├── DEVELOPMENT_PLAN.md
│   ├── PR_GUIDELINES.md
│   └── README_DRAFT.md
├── gym_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── training/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Modelos previstos

- `Atleta`: usuario customizado herdando de `AbstractUser`.
- `GrupoMuscular`: classificacao dos exercicios.
- `Exercicio`: catalogo de exercicios.
- `FichaDeTreino`: plano de treino de um atleta.
- `ItemFichaDeTreino`: modelo intermediario entre ficha e exercicio.

## Funcionalidades previstas

- Cadastro e login de atletas.
- CRUD de grupos musculares.
- CRUD de exercicios.
- CRUD de fichas de treino.
- Inclusao de exercicios em fichas por meio de itens de treino.
- Interface com Bootstrap.

## Status

Projeto em fase de documentacao inicial. Nenhum codigo Django foi implementado nesta etapa.
