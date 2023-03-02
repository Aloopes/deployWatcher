#!/usr/bin/env bash
command -v coverage >/dev/null && coverage erase
command -v python-coverage >/dev/null && python-coverage erase
pytest deployWatcher -v -r sxX