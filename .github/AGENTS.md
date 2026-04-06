---
description: Available custom agents for Soc Ops development
---

# Custom Agents for Soc Ops

## Mandatory Development Checklist
- [ ] **Lint**: uv run ruff check .
- [ ] **Test**: uv run pytest
- [ ] **Run**: uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Specialized agents for Soc Ops development. Select from VS Code chat dropdown.

## Game Development
- **Quiz Master**: Generate bingo questions/themes
- **Game Logic Agent**: Implement bingo mechanics
- **API Agent**: Build FastAPI endpoints

## Development Workflow
- **TDD Supervisor**: Full TDD cycle orchestration
- **TDD Red**: Write failing tests
- **TDD Green**: Minimal implementation
- **TDD Refactor**: Code improvement

## Design & UI
- **Pixel Jam**: UI design iteration
- **UI Review**: Interface feedback

## Usage
1. Open chat panel
2. Select agent from dropdown
3. Provide task description
4. Follow guided workflow

**Tips:**
- New features → TDD Supervisor
- Questions → Quiz Master
- API work → API Agent
- UI design → Pixel Jam
