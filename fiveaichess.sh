#!/usr/bin/env bash
# GUIs like En Croissant launch this script without activating a virtual
# environment, so use the project's .venv interpreter explicitly.
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
# Python 3.13+ skips .pth files with the macOS "hidden" flag, which can break
# the editable install, so put the package on the path directly.
export PYTHONPATH="$PROJECT_DIR${PYTHONPATH:+:$PYTHONPATH}"
exec "$PROJECT_DIR/.venv/bin/python" -m fiveaichess.engines.example_engine
