SHELL   := /bin/bash
OUTPUT  := engincan_varan_cv.pdf
PYTHON  := python3

.PHONY: all deps build clean

all: build

## Install tectonic (run once)
deps:
	@command -v brew >/dev/null 2>&1 || \
		(echo "Error: Homebrew not found — install from https://brew.sh" && exit 1)
	@if command -v tectonic >/dev/null 2>&1; then \
		echo "✓ tectonic already installed"; \
	else \
		echo "→ Installing tectonic..."; \
		brew install tectonic; \
		echo "✓ Done"; \
	fi

## Build the PDF (tectonic auto-downloads any missing LaTeX packages)
build:
	@$(PYTHON) build_cv.py

## Remove generated PDF
clean:
	@rm -f $(OUTPUT)
	@echo "✓ Cleaned"
