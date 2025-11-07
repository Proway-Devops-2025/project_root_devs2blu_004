# Repository Guidelines

## Project Structure & Module Organization
- `app/` hosts the end-user Python application (`main.py`, `requirements.txt`, static assets such as `index.html`). Treat it as the reference for runtime behavior.
- `core/` is reserved for the core submodule. Always run `git submodule update --init --recursive` after cloning so shared logic is available.
- `containers/` aggregates Docker-orchestration assets (e.g., future `docker-compose.yml` plus Nginx/Backend/Frontend Dockerfiles). Keep container configs isolated here.
- Top-level docs (`README.md`, `AGENTS.md`) describe workflows; never mix source files into the repo root.

## Build, Test, and Development Commands
- Install Python deps: `pip install -r app/requirements.txt`.
- Run the local app: `python app/main.py` from the repo root (ensures relative imports resolve).
- Container workflows: from `containers/`, run `docker compose up --build` once Compose files exist. Map `/frontend` to port 3000 and `/backend` to 8000 behind the Nginx proxy per container spec.
- Sync submodules before pushing: `git submodule update --remote core`.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation. Prefer type hints and f-strings for clarity.
- Name Python modules/functions in `snake_case`, classes in `PascalCase`, constants in `UPPER_SNAKE_CASE`.
- Keep HTML/CSS/JS assets lightweight and colocated under `app/` or a future `app/static/` subtree; use kebab-case for file names.
- Docker services and Compose profiles should use lowercase hyphenated names (`frontend-app`, `backend-api`, `edge-nginx`).

## Testing Guidelines
- Place automated tests under `app/tests/` mirroring the package structure (`test_feature_x.py`). Use `pytest` (add it to `requirements-dev.txt` when created).
- Write descriptive test names (`test_handles_invalid_payload`) and favor fixtures for submodule data.
- Strive for coverage of all core-to-app integration points before opening a PR; document any skipped cases in the PR description.

## Commit & Pull Request Guidelines
- Base commit titles on the existing history: short, imperative, scoped summaries (`frontend: add navbar render`). Keep body lines wrapped at 72 characters and reference issue IDs when relevant.
- For pull requests, include: purpose statement, testing evidence (commands + outputs), impact on containers/submodules, and screenshots for UI changes.
- Rebase onto the latest `main` (or the active GitFlow branch) before requesting review, resolving submodule pointers explicitly.

## Security & Configuration Tips
- Never commit secrets; use `.env` files referenced via Docker Compose and add them to `.gitignore`.
- When exposing ports, verify Nginx routes `/frontend` → `3000` and `/backend` → `8000` while keeping HTTPS termination confined to the edge container.
