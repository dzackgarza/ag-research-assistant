PYTHON ?= python3
REPO ?= dzackgarza/ag-research-assistant
BRANCH ?= main

.PHONY: build check publish-plan publish-api

build:
	$(PYTHON) scripts/build_style_guide.py

check:
	$(PYTHON) scripts/publish.py validate

publish-plan:
	@test -n "$(BASE)" || { echo "BASE=<reviewed upstream commit> is required" >&2; exit 2; }
	$(PYTHON) scripts/publish.py manifest --base "$(BASE)" --repo "$(REPO)" --branch "$(BRANCH)"

publish-api:
	@test -n "$(BASE)" || { echo "BASE=<expected current remote commit> is required" >&2; exit 2; }
	$(PYTHON) scripts/publish.py publish --base "$(BASE)" --repo "$(REPO)" --branch "$(BRANCH)"
