---
description: Workspace instructions for the Soc Ops bingo application development
---

# Soc Ops - Social Bingo Application

## Overview
Soc Ops is a web-based social bingo game built with FastAPI and HTMX. Players create bingo cards with icebreaker questions and find other players who match the prompts to complete lines and win.

## Tech Stack
- **Backend**: FastAPI (Python) with session management
- **Frontend**: HTMX for dynamic interactions, Jinja2 templates
- **Styling**: Custom CSS utilities (Tailwind-like classes)
- **Development**: uv for dependency management, ruff for linting
- **Testing**: pytest with comprehensive test coverage

## Development Guidelines

### Code Quality
- Use type hints and docstrings
- Follow PEP 8 style guidelines
- Write tests for new features
- Use immutable data structures where possible

### Architecture
- Session-based game state (no database required)
- RESTful API endpoints with HTMX integration
- Modular code structure in app/ directory
- Static files served from app/static/

### Game Rules
- 5x5 bingo grid with center free space
- Win by completing rows, columns, or diagonals
- Questions should be inclusive and conversation-starting
- Avoid sensitive topics (health, politics, relationships)

### Browser Usage
- HTMX requires full browser for functionality
- Do NOT use VS Code Simple Browser for preview
- Open http://localhost:8000 in external browser

## File Structure
- pp/main.py - FastAPI application
- pp/game_logic.py - Bingo mechanics
- pp/templates/ - Jinja2 HTML templates
- pp/static/ - CSS and JS assets
- 	ests/ - Test suite
- .github/instructions/ - Specialized instruction files
- .github/agents/ - Custom agent definitions

## Available Agents
See AGENTS.md for specialized agents available in this workspace.
