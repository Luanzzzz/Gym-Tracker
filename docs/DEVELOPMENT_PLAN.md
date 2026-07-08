# Plano de Desenvolvimento

## Visao geral

O Gym Tracker sera implementado em fases pequenas. Cada fase deve ser feita em uma branch propria, revisada em um PR separado e composta por commits atomicos.

O objetivo e manter o historico simples de revisar, com cada PR entregando uma parte funcional e verificavel do sistema.

## Fase 1 - Documentacao inicial

Branch sugerida:

- `docs/project-spec`

Objetivo:

- Criar a documentacao inicial do projeto antes de qualquer implementacao.

Commits atomicos:

- `docs: add project specification and database model`
- `docs: add development plan and PR guidelines`

Criterios de aceite:

- Os arquivos de documentacao inicial existem em `docs/`.
- Nenhum projeto Django foi criado.
- Nenhum arquivo de configuracao foi alterado.
- A documentacao descreve modelos, relacionamentos e escopo.
- O plano cita o diagrama ER obrigatorio no PR de modelagem.

## Fase 2 - Scaffold Django e configuracao base

Branch sugerida:

- `feature/django-scaffold`

Objetivo:

- Criar o projeto Django, configurar ambiente local e preparar a estrutura base.

Commits atomicos esperados:

- Criar projeto Django.
- Configurar app principal.
- Adicionar dependencias iniciais.
- Configurar settings basicos.
- Atualizar README com comandos reais.

Criterios de aceite:

- O servidor local Django inicia sem erro.
- O projeto tem estrutura clara de apps.
- As dependencias estao documentadas.
- Nenhuma regra de negocio complexa foi implementada ainda.

## Fase 3 - Modelagem do banco

Branch sugerida:

- `feature/database-models`

Objetivo:

- Implementar os modelos principais e suas migracoes.

Commits atomicos esperados:

- Implementar `Atleta` herdando de `AbstractUser`.
- Implementar `GrupoMuscular` e `Exercicio`.
- Implementar `FichaDeTreino` e `ItemFichaDeTreino`.
- Criar migracoes.
- Registrar modelos no admin.
- Adicionar ou anexar diagrama ER ao PR.

Criterios de aceite:

- Existem pelo menos 4 modelos.
- `Atleta` herda de `AbstractUser`.
- Existem relacionamentos `ForeignKey`.
- Existe relacionamento N:N por modelo intermediario equivalente.
- Migracoes rodam com sucesso.
- O PR contem o diagrama ER da estrutura do banco de dados.

## Fase 4 - CRUD e navegacao

Branch sugerida:

- `feature/core-crud`

Objetivo:

- Criar as telas principais para listar, visualizar, criar, editar e excluir registros.

Commits atomicos esperados:

- Criar URLs e views para grupos musculares.
- Criar URLs e views para exercicios.
- Criar URLs e views para fichas de treino.
- Criar forms Django.
- Adicionar validacoes simples.

Criterios de aceite:

- O usuario consegue navegar pelas entidades principais.
- CRUD basico funciona para modelos centrais.
- Erros de validacao aparecem nos formularios.
- Views seguem padroes consistentes do Django.

## Fase 5 - Autenticacao e fluxo do atleta

Branch sugerida:

- `feature/athlete-auth-flow`

Objetivo:

- Implementar cadastro, login, logout e telas focadas no atleta autenticado.

Commits atomicos esperados:

- Criar fluxo de registro de atleta.
- Configurar login e logout.
- Restringir fichas por atleta autenticado.
- Criar dashboard simples do atleta.

Criterios de aceite:

- Um atleta consegue se cadastrar.
- Um atleta consegue entrar e sair do sistema.
- O atleta visualiza suas fichas.
- Permissoes avancadas nao sao o foco; apenas restricoes basicas de acesso autenticado.

## Fase 6 - Templates e Bootstrap

Branch sugerida:

- `feature/bootstrap-templates`

Objetivo:

- Melhorar a interface usando Bootstrap ou template pronto compativel com Django.

Commits atomicos esperados:

- Criar layout base.
- Adicionar navegacao principal.
- Padronizar formularios.
- Padronizar tabelas e paginas de detalhe.
- Ajustar mensagens e estados vazios.

Criterios de aceite:

- A interface usa Bootstrap ou template pronto compativel com Django.
- As telas principais compartilham layout consistente.
- Formularios e tabelas sao legiveis.
- A aplicacao pode ser apresentada como portfolio.

## Fase 7 - Testes, ajustes finais e README

Branch sugerida:

- `feature/final-polish`

Objetivo:

- Adicionar testes essenciais, revisar documentacao e preparar entrega final.

Commits atomicos esperados:

- Adicionar testes de models.
- Adicionar testes de views principais.
- Atualizar README final.
- Revisar documentacao de setup.
- Ajustar dados de exemplo, se necessario.

Criterios de aceite:

- Testes principais passam.
- README contem instrucoes reais de instalacao e execucao.
- O projeto esta pronto para avaliacao.
- Escopo continua alinhado com as regras da Mate Academy.
