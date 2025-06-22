#!/bin/bash

# Get the directory of this script (absolute path)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Change to project root where pyproject.toml lives
cd "$SCRIPT_DIR" || exit 1

# Run the compiler with Poetry, forwarding the C file path
poetry run myc "$@"
