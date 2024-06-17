set shell := ["/bin/bash", "-eou", "pipefail", "-c"]

dirs := "datek_app_utils tests"

format *args:
    ruff format {{ args }} {{ dirs }}

lint *args:
    ruff check {{ args }} {{ dirs }}
    mypy {{ dirs }} --check-untyped-defs
