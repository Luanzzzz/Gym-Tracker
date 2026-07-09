# Modelo de Banco de Dados

## Visao geral

O banco de dados do Gym Tracker esta organizado em torno de cinco modelos principais:

- `Atleta`
- `GrupoMuscular`
- `Exercicio`
- `FichaDeTreino`
- `ItemFichaDeTreino`

Essa estrutura cobre autenticacao, catalogo de exercicios, classificacao por grupo muscular e montagem de fichas de treino com relacionamento intermediario.

## Atleta

`Atleta` e o usuario principal do sistema e herda de `AbstractUser`.

Campos implementados:

- Campos herdados de `AbstractUser`, como `username`, `first_name`, `last_name`, `email`, `password`, `is_active` e `is_staff`.
- `birth_date`
- `height`
- `weight`
- `goal`

### Por que herdar de AbstractUser

O uso de `AbstractUser` permite customizar o usuario desde o inicio do projeto sem perder os recursos nativos do Django, como autenticacao, login, logout, permissoes basicas, painel administrativo e compatibilidade com forms de usuario.

Essa escolha evita criar um perfil separado desnecessario para o escopo inicial e atende a regra da Mate Academy de ter um modelo herdando de `AbstractUser`.

## GrupoMuscular

`GrupoMuscular` representa uma categoria anatomica usada para organizar exercicios.

Campos implementados:

- `name`: nome do grupo muscular.
- `description`: texto opcional explicando o grupo ou exemplos de uso.
- `slug`: identificador unico para URLs e administracao.
- `created_at`
- `updated_at`

Relacionamentos:

- Um `GrupoMuscular` pode ter varios `Exercicio`.
- Cada `Exercicio` tera um `ForeignKey` para um `GrupoMuscular` principal.

## Exercicio

`Exercicio` representa um movimento ou atividade que pode ser usado em fichas de treino.

Campos implementados:

- `name`: nome do exercicio.
- `description`: explicacao da execucao.
- `equipment`: equipamento usado, quando aplicavel.
- `difficulty`: nivel do exercicio.
- `muscle_group`: `ForeignKey` para `GrupoMuscular`.
- `slug`: identificador unico.

Relacionamentos:

- Um `Exercicio` pertence a um `GrupoMuscular`.
- Um `Exercicio` pode aparecer em varias `FichaDeTreino`.
- A relacao com `FichaDeTreino` e feita por `ItemFichaDeTreino`.

## FichaDeTreino

`FichaDeTreino` representa um plano de treino de um atleta.

Campos implementados:

- `athlete`: `ForeignKey` para `Atleta`.
- `name`: nome da ficha, como "Treino A" ou "Hipertrofia - Pernas".
- `objective`: objetivo da ficha.
- `notes`: observacoes gerais.
- `exercises`: `ManyToManyField` para `Exercicio` usando `ItemFichaDeTreino` como `through`.
- `created_at`
- `updated_at`

Relacionamentos:

- Uma `FichaDeTreino` pertence a um `Atleta`.
- Uma `FichaDeTreino` contem varios `Exercicio`.
- A associacao com exercicios passa por `ItemFichaDeTreino`.

## ItemFichaDeTreino

`ItemFichaDeTreino` e o modelo intermediario entre `FichaDeTreino` e `Exercicio`.

Campos implementados:

- `workout_plan`: `ForeignKey` para `FichaDeTreino`.
- `exercise`: `ForeignKey` para `Exercicio`.
- `sets`: quantidade de series.
- `reps`: quantidade ou faixa de repeticoes.
- `load`: carga recomendada, quando aplicavel.
- `rest_seconds`: tempo de descanso entre series.
- `order`: posicao do exercicio dentro da ficha.

### Por que usar ItemFichaDeTreino como modelo intermediario

Uma relacao `ManyToMany` simples entre `FichaDeTreino` e `Exercicio` indicaria apenas que um exercicio pertence a uma ficha. Isso nao seria suficiente para um sistema de treino, porque cada exercicio precisa ter dados proprios dentro de cada ficha.

Por exemplo, o exercicio "Supino reto" pode aparecer em uma ficha com 3 series de 10 repeticoes e em outra com 5 series de 5 repeticoes. Esses dados nao pertencem ao exercicio em si; pertencem ao uso do exercicio dentro de uma ficha especifica.

Por isso, `ItemFichaDeTreino` e usado como modelo intermediario equivalente a um `ManyToMany` com `through`, permitindo armazenar informacoes da relacao.

## Relacionamentos resumidos

- `Atleta` 1:N `FichaDeTreino`
- `GrupoMuscular` 1:N `Exercicio`
- `FichaDeTreino` 1:N `ItemFichaDeTreino`
- `Exercicio` 1:N `ItemFichaDeTreino`
- `FichaDeTreino` N:N `Exercicio` por meio de `ItemFichaDeTreino`

## Estrutura esperada para o diagrama ER

O diagrama ER esta documentado em `docs/database/ER_DIAGRAM.md` e contem:

- As cinco tabelas principais.
- Chaves primarias.
- Chaves estrangeiras.
- Relacao entre `FichaDeTreino` e `Exercicio` por meio de `ItemFichaDeTreino`.
- Indicacao visual de cardinalidade, como 1:N e N:N por tabela intermediaria.
