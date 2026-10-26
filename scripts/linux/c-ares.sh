#!/usr/bin/env bash
# Linux -> Android: c-ares. Options: --backend, --ndk, --jobs, --output.
set -euo pipefail
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "${PYTHON:-python3}" "$script_dir/../android-smoke.py" build "$@" --library c-ares
