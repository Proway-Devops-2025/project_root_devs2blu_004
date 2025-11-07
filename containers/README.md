<!--
  Author: Adriano Machado <adriano@maxado.com.br>
  Description: Guidance for building and operating the container stack.
  Last Updated: 2025-11-07
-->
# Containers – Guia de Implementação

## Objetivo
Provisionar uma stack local composta por três serviços: `frontend`, `backend` e `edge-nginx`, garantindo tráfego HTTPS na porta 443 e roteamento reverso para as portas internas 3000 e 8000 respectivamente. A solução deve ser simples de reproduzir via `docker compose`.

## Estrutura Esperada
```
containers/
├── docker-compose.yml
├── backend/
│   └── Dockerfile
├── frontend/
│   └── Dockerfile
└── nginx/
    ├── Dockerfile
    └── default.conf
```
- Mantenha cada serviço isolado em seu diretório para facilitar builds independentes.
- Armazene certificados/keys locais em `nginx/certs/` (adicionados ao `.gitignore`) e referencie-os no compose.

## Requisitos Funcionais
1. **Frontend**  
   - Container baseado em Node.  
   - Expõe porta interna `3000`.  
   - Healthcheck acessando `http://frontend:3000/health`.
2. **Backend**  
   - Pode ser Python FastAPI `app/`.  
   - Porta interna `8000`.  
   - Healthcheck `http://backend:8000/health`.
3. **Edge Nginx**  
   - Termina HTTPS na `443` e, opcionalmente, HTTP na `80` para redirecionar.  
   - Roteia `/frontend` → `frontend:3000` e `/backend` → `backend:8000`.  
   - Garante gzip e headers básicos (`X-Content-Type-Options`, `X-Frame-Options`).

## Requisitos Técnicos
- Arquivo `docker-compose.yml` na raiz de `containers/` declarando rede bridge única e volumes nomeados para cache (p.ex. `frontend_node_modules`).  
- Usar build args mínimos; preferir multi-stage para reduzir tamanho.  
- Variáveis sensíveis em arquivos `.env` (não versionados) ou via `docker compose --env-file`.
- Comando principal esperado:
  ```bash
  docker compose up --build
  ```
  Deve subir os três serviços e expor apenas a porta `443` para o host (além da `80` se necessário para redirect).

## Próximos Passos
- [ ] Criar Dockerfiles compatíveis com `linux/amd64`.  
- [ ] Definir scripts `start-dev.sh`/`start-prod.sh` se comportamentos divergem.  
- [ ] Documentar no `AGENTS.md` qualquer alteração de portas ou variáveis exigidas pelos módulos `app/` e `core/`.


## Deve conter um pagina Hello World com as palavras "Pizza da Turma DevOps" 
