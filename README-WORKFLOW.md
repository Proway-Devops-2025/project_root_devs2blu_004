# README - Fluxo de Tags e Changelog

Documento de referencia para o workflow `Auto Tag Develop` definido em `.github/workflows/develop-auto-tag.yml`. Este fluxo automatiza o versionamento da branch `develop`, gera changelog e publica tags no padrao `v1.0.x`.

## Visao geral

- **Objetivo**: garantir que cada merge ou push em `develop` produza um changelog atualizado e uma nova tag sequencial (`v1.0.0`, `v1.0.1`, ...).
- **Acionadores**: `push` em `develop` ou execucao manual via `workflow_dispatch`.
- **Escopo**: apenas commits em `develop`. A branch `main` nao e modificada automaticamente.
- **Permissoes**: workflow usa `contents: write` para criar commits/tags no repositorio.

## Etapas executadas

1. **Checkout completo**  
   Usa `actions/checkout@v4` com `fetch-depth: 0` para ter historico e tags locais.

2. **Calculo da proxima tag**  
   - Busca todas as tags que comecam com o prefixo `v1.0.`.  
   - Ordena de forma decrescente pela porcao numerica (`v1.0.12` > `v1.0.9`).  
   - Caso nao exista tag, inicia em `v1.0.0`.  
   - Se o ultimo sufixo nao for numerico, o job falha para evitar saltos incorretos.

3. **Atualizacao do changelog**  
  - Determina o intervalo de commits entre a ultima tag e o `HEAD` atual (ou todo o historico se nao houver tag).  
  - Extrai os assuntos (`%s`) de cada commit e formata como lista `- Mensagem`.  
  - Garante que o arquivo `CHANGELOG` exista e reconstrui o conteudo com um cabecalho padrao:
    ```text
    # Changelog

    ## v1.0.X - AAAA-MM-DD

    - Mensagem do commit
    ```
  - Se nao houver commits novos, o workflow encerra sem gerar tag.

4. **Commit do changelog**  
   - Configura o autor como `github-actions[bot]`.  
   - Faz `git add CHANGELOG`, `git commit` e `git push origin HEAD:develop`.  
   - A condicao `if: github.actor != 'github-actions[bot]'` impede que o proprio bot reexecute o fluxo em loop.

5. **Criacao e push da tag**  
   - Executado apenas se houve commit no changelog.  
   - Cria uma tag anotada `git tag -a v1.0.X -m "Tag automatica para merge na develop"`.  
   - Faz `git push origin v1.0.X`.  
   - Se a tag ja existir (condicao rara, mas validada), nada e feito.

## Como executar manualmente

1. Acesse a aba **Actions** no GitHub.  
2. Escolha o workflow **Auto Tag Develop**.  
3. Clique em **Run workflow** e confirme a branch `develop`.  
4. Aguarde a conclusao para ver logs de changelog/tag.

## Boas praticas e manutencao

- **Mensagens de commit objetivas**: o changelog usa o assunto do commit; escreva descricoes claras.  
- **Protecoes da branch**: garanta que o usuario `github-actions[bot]` possa fazer push na `develop` (por exemplo, habilitando _Allow GitHub Actions to push_ nas regras).  
- **Mudanca de prefixo**: altere a variavel `TAG_PREFIX` na etapa "Compute next v1.0.x tag" caso precise de nova serie (`v1.1.`). Recomenda-se criar um novo arquivo `CHANGELOG` ou limpar o atual antes de trocar a numeracao.  
- **Rollback**: se precisar excluir uma tag criada automaticamente, remova tanto local quanto remotamente (`git tag -d v1.0.X && git push origin :refs/tags/v1.0.X`) e ajuste o changelog manualmente.

## Solucao de problemas

- **Workflow nao cria tag**: verifique se houve commits desde a ultima tag; sem commits nao ha tag nem changelog novo.  
- **Erro em sufixo numerico**: confirme se todas as tags com prefixo `v1.0.` tem sufixo apenas numerico. Remova ou renomeie qualquer tag fora do padrao.  
- **Loop infinito**: se remover o `if: github.actor != 'github-actions[bot]'`, o workflow pode reexecutar indefinidamente porque o bot gera novos commits. Mantenha esse filtro.  
- **Conflitos no changelog**: caso edicoes manuais ocorram entre runs, resolva os conflitos e reexecute o workflow manualmente para alinhar o historico.

Este documento deve ser atualizado sempre que o workflow sofrer alteracoes de logica, prefixo de tags ou arquivos manipulados.
