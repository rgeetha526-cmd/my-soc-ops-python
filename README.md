# 🎉 Soc Ops - Social Bingo Game

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![HTMX](https://img.shields.io/badge/HTMX-1.9+-orange.svg)](https://htmx.org/)

> **Break the ice and connect with people!** Soc Ops is a fun, interactive social bingo game designed for in-person mixers and events. Create bingo cards filled with engaging icebreaker questions, find people who match the prompts, and get 5 in a row to win!

![Soc Ops Demo](https://via.placeholder.com/800x400?text=Soc+Ops+Demo+Screenshot) <!-- Replace with actual screenshot -->

## ✨ Features

- 🎯 **Interactive Bingo Cards**: 5x5 grids with customizable icebreaker questions
- 👥 **Social Networking**: Connect with attendees by finding matches for each prompt
- 🏆 **Winning Mechanics**: Complete rows, columns, or diagonals to score points
- 🌐 **Web-Based**: Built with FastAPI and HTMX for smooth, dynamic interactions
- 📱 **Responsive Design**: Works great on desktops, tablets, and mobile devices
- 🎨 **Customizable Themes**: Tailwind-like CSS utilities for easy styling
- 🔒 **Session-Based**: No database required - everything runs in memory
- 🧪 **Well-Tested**: Comprehensive test suite with pytest

## 🚀 Quick Start

Get Soc Ops running in minutes!

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rgeetha526-cmd/my-soc-ops-python.git
   cd my-soc-ops-python
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Open your browser:**
   Visit [http://localhost:8000](http://localhost:8000) and start playing!

### 🧪 Running Tests

```bash
uv run pytest
```

### 🧹 Linting

```bash
uv run ruff check .
```

## 📚 Lab Guide

This project includes a comprehensive workshop guide for learning advanced development techniques with GitHub Copilot and multi-agent systems.

| Part | Title | Description |
|------|-------|-------------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | Get started with prerequisites and project overview |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | Configure your development environment |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | Build beautiful UIs with HTMX and custom CSS |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | Create engaging icebreaker questions |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | Learn collaborative coding with AI agents |

> 📝 Lab guides are also available in the [`workshop/`](workshop/) folder for offline reading.

🌐 **Multilingual Support:** [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please read our [Contributing Guide](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using [FastAPI](https://fastapi.tiangolo.com/) and [HTMX](https://htmx.org/)
- Inspired by social icebreakers and classic bingo games
- Part of the GitHub Copilot Developer Days workshop series

---

**Ready to break the ice?** Start your Soc Ops adventure today! 🎲
