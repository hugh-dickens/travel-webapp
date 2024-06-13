# Example Makefile

# Variables
BACKEND_DIR := backend
FRONTEND_DIR := frontend

# Backend tasks
backend-format:
	cd $(BACKEND_DIR) && source venv/Scripts/activate && black . && isort .

backend-lint:
	cd $(BACKEND_DIR) && source venv/Scripts/activate && pylint **/*.py

# Frontend tasks
frontend-format:
	cd $(FRONTEND_DIR) && prettier --write "src/**/*.{js,jsx,ts,tsx}"

frontend-lint:
	cd $(FRONTEND_DIR) && eslint "src/**/*.{js,jsx,ts,tsx}"

# Combined tasks
format: backend-format frontend-format
lint: backend-lint frontend-lint

# Pre-commit hook installation
install-hooks:
	pre-commit install
