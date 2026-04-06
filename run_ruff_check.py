#!/usr/bin/env python3
"""Run ruff linter on the codebase."""

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "ruff", "check", "."],
    cwd=".",
    capture_output=False,
)

sys.exit(result.returncode)
