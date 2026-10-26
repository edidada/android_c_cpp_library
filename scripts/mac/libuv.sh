#!/usr/bin/env bash
# mac -> Android: libuv. Windows requires Git Bash.
set -euo pipefail
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python_command="${PYTHON:-python3}"
exec "$python_command" "$script_dir/../android-smoke.py" build "$@" --library libuv
