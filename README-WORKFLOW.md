# README - Fluxo de Tags e Changelog

Documento de referencia para o workflow `Auto Tag Develop` (`.github/workflows/develop-auto-tag.yml`). Ele controla as versoes geradas nas branches `develop` e `main`, alimenta o `CHANGELOG` e publica tags no formato `v<major>.0.<patch>`.

## Visao geral

- **Objetivo**: cada entrega em `develop` gera uma nova tag incremental (patch) e cada PR mergeada em `main` cria uma nova versao major, reiniciando a contagem de patch.
- **Acionadores**: `push` em `develop` ou `main`, `pull_request` fechada/mergeada para essas branches e execucao manual (`workflow_dispatch`) com selecao explicita da branch.
- **Escopo**: o workflow altera o `CHANGELOG` e cria tags diretamente na branch alvo (develop ou main). A outra branch nao e tocada automaticamente.
- **Permissoes**: `contents: write` para permitir commits do bot e criacao de tags remotas.

## Regras de versionamento

1. **Formato**: sempre `v<major>.0.<patch>`. O segundo campo permanece `0` para simplificar e focar apenas em major/patch.
2. **Develop (patch)**: todo push/merge em `develop` incrementa o patch do maior `major` existente. Sem tags anteriores, inicia em `v1.0.0`.
3. **Main (major)**: merge de PR em `main` incrementa o `major` global (ex.: `v1.0.x` -> `v2.0.0`). Caso nao existam commits novos desde a ultima tag, o changelog recebe uma anotacao padrao para manter o historico consistente.
4. **Workflow dispatch**: aceita o input `target_branch` (`develop` ou `main`). Se omitido, assume `develop`.

## Etapas executadas

1. **Checkout completo**  
   Utiliza `actions/checkout@v4` com `fetch-depth: 0`, garantindo acesso a todo o historico de commits e tags.

2. **Deteccao da branch e calculo da proxima tag**  
   - Identifica a branch alvo com base no evento (PR, push ou input manual).  
   - Define o tipo de release (`patch` para `develop`, `major` para `main`).  
   - Busca todas as tags `v*.0.*` para achar o maior `major` atual e o ultimo `patch`.  
   - Calcula a proxima tag seguindo as regras acima, sempre validando se o sufixo numerico esta correto.

3. **Atualizacao do changelog**  
   - Coleta os assuntos dos commits desde a ultima tag global (`git log last_tag..HEAD`).  
   - Se nao existirem commits e o release for `major`, insere uma linha padrao `- Release major sem commits adicionais desde a ultima tag.` para registrar o corte.  
   - Reconstrui o arquivo `CHANGELOG`, adicionando o novo bloco no topo:
     ```text
     # Changelog

     ## vX.0.Y - AAAA-MM-DD

     - Mensagem do commit
     ```

4. **Commit do changelog**  
   - Configura o autor como `github-actions[bot]`.  
   - Comita e faz push diretamente para a branch processada (`develop` ou `main`).  
   - A condicao do job assegura que o bot nao reinicie o workflow e que PRs fechadas sem merge sejam ignoradas.

5. **Criacao e push da tag**  
   - Cria uma tag anotada (`git tag -a vX.0.Y ...`) no commit atual.  
   - Faz `git push origin vX.0.Y`.  
   - Caso a tag ja exista, a etapa termina silenciosamente.

## Como executar manualmente

1. Abra a aba **Actions** no GitHub.  
2. Selecione **Auto Tag Develop**.  
3. Clique em **Run workflow** e escolha `develop` ou `main` no campo `target_branch`.  
4. Acompanhe os logs para verificar o novo bloco do changelog e a tag criada.

## Boas praticas e manutencao

- **Mensagens de commit claras**: o changelog usa apenas o assunto (`%s`), portanto escreva titulos descritivos.  
- **Protecoes de branch**: habilite permissoes para `github-actions[bot]` fazer push em `develop` e `main`.  
- **Personalizacao do esquema**: caso deseje introduzir outro padrao (ex.: incluir numero de minor), adapte o script da etapa "Compute next tag".  
- **Rollback de tags**: para remover uma versao, use `git tag -d vX.0.Y` e `git push origin :refs/tags/vX.0.Y`, ajustando o `CHANGELOG` manualmente em seguida.

## Solucao de problemas

- **Workflow nao cria tag**: confirme se ha commits desde a ultima tag (para releases patch). Para releases major, uma entrada padrao e criada mesmo sem commits.  
- **Tags fora do padrao**: qualquer tag que nao respeite `v<numero>.0.<numero>` pode quebrar a ordenacao; renomeie-as ou remova-as.  
- **Loop infinito**: mantenha o filtro `github.actor != 'github-actions[bot]'` para impedir reexecucao desencadeada pelos commits do bot.  
- **Conflitos no `CHANGELOG`**: resolva manualmente e reexecute o workflow (ou rode via `workflow_dispatch`) para reescrever o topo do arquivo.

Atualize este documento sempre que o workflow sofrer mudancas estruturais.
