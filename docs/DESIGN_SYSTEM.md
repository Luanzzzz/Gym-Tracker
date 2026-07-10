# Design System - Gym Tracker

Status: implementado com Bootstrap 5, Django Templates e CSS leve em `static/training/css/styles.css`.

## 1. Identidade visual

Nome do produto:

- Gym Tracker

Estilo visual:

- Moderno.
- Limpo.
- Esportivo.
- Profissional.
- Direto e facil de usar.

O visual deve transmitir organizacao e confianca, com foco em acompanhamento de treino, rotina de academia e clareza das informacoes.

O projeto deve evitar:

- Visual exageradamente gamer.
- Interfaces muito escuras ou agressivas.
- Efeitos visuais complexos.
- Excesso de animacoes.
- Layouts dificeis de manter com Django Templates.

## 2. Paleta de cores

A paleta deve aproveitar classes do Bootstrap sempre que possivel, evitando CSS customizado pesado.

### Cor principal

Uso recomendado:

- Acoes principais.
- Links importantes.
- Destaques de navegacao.
- Botoes primarios.

Sugestao:

- Bootstrap `primary`
- Hex sugerido, se houver customizacao futura: `#0D6EFD`

### Cor secundaria

Uso recomendado:

- Elementos de apoio.
- Botoes secundarios.
- Textos e componentes menos prioritarios.

Sugestao:

- Bootstrap `secondary`
- Hex sugerido, se houver customizacao futura: `#6C757D`

### Cor de fundo

Uso recomendado:

- Fundo geral das paginas.
- Areas de dashboard.
- Listagens.

Sugestao:

- Bootstrap `light`
- Hex sugerido, se houver customizacao futura: `#F8F9FA`

### Cor de texto

Uso recomendado:

- Texto principal.
- Titulos.
- Conteudo de tabelas e cards.

Sugestao:

- Bootstrap `dark`
- Hex sugerido, se houver customizacao futura: `#212529`

### Alertas, sucesso e erro

Usar classes Bootstrap nativas:

- Sucesso: `alert alert-success`, `text-success`, `btn-success`, `badge text-bg-success`
- Erro: `alert alert-danger`, `text-danger`, `btn-danger`, `badge text-bg-danger`
- Alerta: `alert alert-warning`, `text-warning`, `btn-warning`, `badge text-bg-warning`
- Informacao: `alert alert-info`, `text-info`, `btn-info`, `badge text-bg-info`

## 3. Tipografia

O projeto deve usar fontes simples, seguras e faceis de carregar.

Opcoes recomendadas:

- Fonte padrao do Bootstrap.
- Fonte segura do sistema: `system-ui, -apple-system, "Segoe UI", sans-serif`.
- Google Font simples, se necessario: `Inter` ou `Roboto`.

Evitar:

- Muitas familias de fontes.
- Fontes decorativas.
- Tipografia com aparencia de jogo ou evento esportivo extremo.

### Hierarquia sugerida

Titulos de pagina:

- Usar `h1` ou classe Bootstrap equivalente.
- Texto curto e direto, como "Fichas de treino" ou "Exercicios".

Subtitulos e secoes:

- Usar `h2` ou `h3`.
- Separar areas como resumo, detalhes e formularios.

Textos comuns:

- Usar tamanho padrao do Bootstrap.
- Manter contraste suficiente com o fundo.

Textos auxiliares:

- Usar classes como `text-muted` ou `small`.
- Aplicar em descricoes, datas, observacoes e mensagens secundarias.

## 4. Componentes

### Navbar

A navbar deve ser simples e persistente nas paginas principais.

Itens recomendados:

- Logo ou nome `Gym Tracker`.
- Link para dashboard.
- Link para grupos musculares.
- Link para exercicios.
- Link para fichas de treino.
- Area de usuario com login, logout ou nome do atleta.

Classes Bootstrap recomendadas:

- `navbar`
- `navbar-expand-lg`
- `navbar-light` ou `navbar-dark`
- `bg-light` ou `bg-primary`

### Sidebar ou menu simples

Para a primeira versao, um menu simples na navbar pode ser suficiente.

Se o dashboard crescer, pode ser usada uma sidebar simples para:

- Dashboard.
- Atletas.
- Grupos musculares.
- Exercicios.
- Fichas de treino.

A sidebar deve ser responsiva e nao deve dificultar o uso em mobile.

### Cards de dashboard

Cards devem resumir informacoes importantes:

- Total de fichas de treino.
- Total de exercicios cadastrados.
- Total de grupos musculares.
- Ultimas fichas criadas.

Classes Bootstrap recomendadas:

- `card`
- `card-body`
- `card-title`
- `card-text`
- `row`
- `col`

### Tabelas

Tabelas devem ser usadas em listagens administrativas e de catalogo.

Uso recomendado:

- Lista de exercicios.
- Lista de grupos musculares.
- Lista de fichas de treino.

Classes Bootstrap recomendadas:

- `table`
- `table-striped`
- `table-hover`
- `table-responsive`

As tabelas devem ter acoes claras, como visualizar, editar e excluir.

### Botoes

Usar botoes Bootstrap padronizados:

- Acao principal: `btn btn-primary`
- Acao secundaria: `btn btn-secondary`
- Confirmar ou salvar: `btn btn-success`
- Cancelar ou voltar: `btn btn-outline-secondary`
- Excluir: `btn btn-danger`

Evitar muitos estilos diferentes de botao na mesma tela.

### Formularios

Formularios devem seguir o padrao Bootstrap.

Classes recomendadas:

- `form-label`
- `form-control`
- `form-select`
- `form-check`
- `invalid-feedback`

Regras:

- Labels claros.
- Mensagens de erro proximas ao campo.
- Botoes de salvar e cancelar no final do formulario.
- Campos obrigatorios bem indicados.

### Badges

Badges devem indicar status ou classificacoes curtas.

Exemplos:

- Nivel do exercicio: `badge text-bg-info`
- Grupo muscular: `badge text-bg-primary`
- Nivel ou objetivo: `badge text-bg-info`

### Alertas

Alertas devem comunicar resultado de acoes:

- Ficha criada com sucesso.
- Exercicio atualizado.
- Erro de validacao.
- Confirmacao de exclusao.

Usar mensagens do Django integradas com classes Bootstrap:

- `alert alert-success`
- `alert alert-danger`
- `alert alert-warning`
- `alert alert-info`

### Pagina de login

A pagina de login deve ser objetiva e centralizada.

Elementos recomendados:

- Nome Gym Tracker.
- Card simples com formulario de login.
- Campos de usuario e senha.
- Botao principal para entrar.
- Link para cadastro, se o fluxo de registro existir.

Evitar:

- Fundo visualmente pesado.
- Muitos textos explicativos.
- Layout com excesso de imagens.

### Paginas de listagem

Paginas de listagem devem conter:

- Titulo claro.
- Botao de criar novo item.
- Tabela ou cards, conforme o conteudo.
- Campo de busca ou filtro simples, se necessario.
- Estado vazio com mensagem curta.

Exemplos:

- Listagem de exercicios.
- Listagem de grupos musculares.
- Listagem de fichas de treino.

### Paginas de detalhe

Paginas de detalhe devem mostrar informacoes organizadas por blocos.

Exemplo para ficha de treino:

- Nome da ficha.
- Atleta.
- Objetivo.
- Observacoes gerais.
- Lista ordenada de exercicios.
- Series, repeticoes, carga, descanso e ordem.

Acoes recomendadas:

- Editar.
- Excluir.
- Voltar para listagem.

### Paginas de confirmacao de delete

Paginas de delete devem ser simples e seguras.

Elementos recomendados:

- Mensagem clara informando o item que sera excluido.
- Botao perigoso com `btn btn-danger`.
- Botao de cancelar com `btn btn-outline-secondary`.
- Texto curto explicando que a acao pode remover dados relacionados, quando aplicavel.

## 5. Templates Bootstrap recomendados

O projeto deve priorizar componentes prontos do Bootstrap.

Componentes recomendados:

- Navbar.
- Cards.
- Tables.
- Forms.
- Buttons.
- Badges.
- Alerts.
- Pagination.
- Breadcrumbs, se houver navegacao mais profunda.

Nao instalar bibliotecas visuais desnecessarias na primeira versao.

Evitar:

- Frameworks JavaScript pesados.
- Temas muito complexos.
- Bibliotecas de componentes que dupliquem o Bootstrap.
- Customizacoes visuais que dificultem manutencao.

Se um template pronto for usado, ele deve ser:

- Compativel com Bootstrap.
- Facil de adaptar para Django Templates.
- Leve.
- Responsivo.
- Sem dependencia obrigatoria de JavaScript pesado.

## 6. Regras de manutencao

### Simplicidade

Manter o frontend simples e focado nas tarefas principais:

- Consultar fichas.
- Gerenciar exercicios.
- Organizar grupos musculares.
- Montar treinos.

### JavaScript

Evitar JavaScript pesado.

Usar JavaScript apenas quando houver ganho claro de usabilidade, como:

- Confirmacoes simples.
- Pequenas interacoes de formulario.
- Componentes Bootstrap que dependam de comportamento nativo.

### Responsividade

Priorizar layout responsivo desde o inicio.

Regras:

- Usar grid Bootstrap.
- Testar telas em mobile e desktop.
- Evitar tabelas quebradas em telas pequenas.
- Usar `table-responsive` quando necessario.

### Consistencia

Manter consistencia entre telas:

- Mesma navbar.
- Mesmo padrao de botoes.
- Mesma organizacao de formularios.
- Mesmas classes de alerta.
- Mesmos nomes para acoes recorrentes, como "Salvar", "Cancelar", "Editar" e "Excluir".

### Manutencao

Como o projeto e feito com Django Templates, os layouts devem permanecer organizados em templates reutilizaveis:

- Template base.
- Blocos para titulo e conteudo.
- Includes para navbar, mensagens e componentes repetidos.

Esta documentacao orienta a manutencao visual do projeto implementado.
