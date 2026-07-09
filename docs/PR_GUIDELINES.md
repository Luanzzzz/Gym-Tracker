# Diretrizes de Pull Request

## Padrao de titulo

Use titulos curtos, no imperativo ou formato convencional, indicando o tipo da mudanca.

Exemplos:

- `Docs: add initial Gym Tracker project documentation`
- `Feature: add database models`
- `Feature: add workout CRUD views`
- `Fix: adjust exercise form validation`
- `Tests: add model tests`

## Padrao de descricao

Cada PR deve explicar objetivamente:

- O que foi alterado.
- Por que a alteracao foi feita.
- Como testar ou revisar.
- Quais pontos ainda ficam fora do escopo.

Modelo sugerido:

```md
## Summary
- ...

## How to test
- ...

## Checklist
- [ ] O escopo do PR esta claro.
- [ ] Os commits sao atomicos.
- [ ] A aplicacao foi verificada localmente, quando aplicavel.
- [ ] A documentacao foi atualizada, quando aplicavel.
```

## Checklist obrigatorio

Antes de abrir ou marcar um PR como pronto para revisao:

- [ ] O PR tem titulo claro.
- [ ] A descricao explica o objetivo da mudanca.
- [ ] O PR nao mistura assuntos independentes.
- [ ] Os commits sao pequenos e atomicos.
- [ ] Arquivos gerados desnecessarios nao foram incluidos.
- [ ] Nao ha alteracoes fora do escopo.
- [ ] A verificacao local foi executada, quando aplicavel.
- [ ] A documentacao foi atualizada, quando a mudanca exigir.

## Checklist especifico para PR de modelagem

O PR de modelagem do banco deve conter:

- [ ] Modelo `Atleta` herdando de `AbstractUser`.
- [ ] Pelo menos 4 modelos no projeto.
- [ ] Relacionamentos `ForeignKey`.
- [ ] Relacionamento `ManyToMany` ou modelo intermediario equivalente.
- [ ] `ItemFichaDeTreino` como modelo intermediario entre ficha e exercicio.
- [ ] Migracoes criadas e verificadas.
- [ ] Modelos registrados no Django admin, se fizer sentido para a fase.
- [ ] Diagrama ER anexado na descricao do PR.

## Lembrete sobre o diagrama ER

O PR de modelagem deve anexar o diagrama ER da estrutura do banco de dados. O diagrama deve mostrar as entidades principais, chaves estrangeiras e cardinalidades.

Sugestao de texto para o PR de modelagem:

```md
## Database diagram

Diagrama ER anexado abaixo:

<!-- anexar imagem ou link do diagrama ER aqui -->
```

## PR final de entrega

Titulo sugerido:

```text
Chore: prepare Gym Tracker portfolio delivery
```

Descricao final pronta:

- Ver `docs/FINAL_PR_DESCRIPTION.md`.
