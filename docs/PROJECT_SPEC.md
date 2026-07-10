# Gym Tracker - Especificacao Inicial

## Visao geral

Gym Tracker e uma aplicacao web em Django para gerenciar treinos de academia. O sistema permite o cadastro de atletas, grupos musculares, exercicios e fichas de treino compostas por exercicios organizados.

O projeto foi desenvolvido como portfolio para a Mate Academy, com complexidade semelhante ao projeto de Servico de Taxi, mas aplicado ao dominio de treinos e sem copiar o tema, entidades ou fluxos principais daquele projeto.

## Objetivo do sistema

O objetivo e entregar uma aplicacao CRUD completa, com autenticacao de usuario, relacionamentos entre modelos e interface baseada em templates Django com Bootstrap.

O usuario principal e o atleta, que pode consultar ou gerenciar fichas de treino contendo exercicios de diferentes grupos musculares. O sistema tambem demonstra dominio de models, views, URLs, templates, forms, administracao Django e organizacao de projeto.

## Escopo

Incluido no escopo implementado:

- Autenticacao de atletas com usuario customizado.
- Cadastro de grupos musculares, como Peito, Costas, Pernas, Ombros, Biceps, Triceps e Abdomen.
- Cadastro de exercicios associados a grupos musculares.
- Cadastro de fichas de treino associadas a um atleta.
- Inclusao de exercicios em fichas de treino por meio de um modelo intermediario.
- Registro de detalhes do exercicio dentro da ficha, como ordem, series, repeticoes, carga e descanso.
- Listagens, detalhes, criacao, edicao e exclusao para as entidades principais.
- Interface simples com Bootstrap.
- Diagrama ER da estrutura do banco de dados no PR de modelagem.

Fora do escopo inicial:

- Permissoes avancadas por perfil.
- Planos pagos, assinaturas ou integracoes com pagamento.
- Monitoramento de treinos em tempo real.
- Aplicativo mobile.
- API REST publica.
- Integracoes com dispositivos, relogios ou sensores.

## Funcionalidades principais

### Atletas

- Usar `Atleta` como usuario customizado do sistema.
- Autenticar atleta com login e senha.
- Guardar dados basicos do perfil, como nome, email e informacoes simples de treino.
- Relacionar cada ficha de treino ao atleta responsavel.

### Grupos musculares

- Cadastrar grupos musculares usados para classificar exercicios.
- Listar grupos musculares com seus exercicios associados.
- Facilitar filtros e navegacao por area do corpo.

### Exercicios

- Cadastrar exercicios com nome, descricao e grupo muscular principal.
- Permitir que exercicios sejam reutilizados em varias fichas de treino.
- Servir como catalogo base para montar fichas.

### Fichas de treino

- Criar fichas de treino para atletas.
- Definir nome, objetivo e observacoes gerais da ficha.
- Associar varios exercicios a uma ficha.
- Exibir a ficha com exercicios em ordem planejada.

### Itens da ficha de treino

- Representar a prescricao de um exercicio dentro de uma ficha.
- Guardar dados especificos daquela ficha, como series, repeticoes, carga, descanso e ordem.
- Permitir que o mesmo exercicio apareca em fichas diferentes com prescricoes diferentes.

## Regras da atividade da Mate Academy

- O projeto deve ter pelo menos 4 modelos.
- Um modelo deve herdar de `AbstractUser`.
- O projeto deve ter complexidade semelhante ao projeto Servico de Taxi da Mate Academy.
- O tema nao deve copiar o projeto de taxi.
- O banco deve ter relacionamentos `ForeignKey`.
- O banco deve ter relacionamento `ManyToMany` ou modelo intermediario equivalente.
- Permissoes avancadas nao devem ser o foco.
- O PR final deve conter um diagrama da estrutura do banco de dados.
- O frontend deve usar Bootstrap ou templates prontos compativeis com Django.

## Equivalencias com o projeto Servico de Taxi

O Gym Tracker deve demonstrar competencias parecidas com o projeto de Servico de Taxi, mas usando entidades do dominio de academia:

- Em vez de motorista ou usuario operacional, o sistema usa `Atleta` como usuario customizado.
- Em vez de carros ou fabricantes, o sistema usa `Exercicio` e `GrupoMuscular` como catalogo reutilizavel.
- Em vez de associar motoristas a carros, o sistema associa atletas a fichas de treino.
- Em vez de um relacionamento simples sem contexto, a ficha usa `ItemFichaDeTreino` como modelo intermediario para guardar dados especificos da relacao entre ficha e exercicio.
- Em vez de permissoes avancadas, o foco e CRUD, autenticacao, relacionamento entre modelos, templates e organizacao do projeto.

Essa equivalencia garante complexidade suficiente para avaliacao sem reaproveitar tema, nomes ou fluxo do projeto de taxi.
