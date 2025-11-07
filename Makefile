.PHONY: env html clean
ENV_NAME := myst

env:
	@echo ">> Ensuring conda env '$(ENV_NAME)' matches environment.yml"
	@if conda env list | awk '{print $$1}' | grep -qx '$(ENV_NAME)'; then \
		echo ">> Updating existing env $(ENV_NAME)"; \
		conda env update -n $(ENV_NAME) -f environment.yml --prune; \
	else \
		echo ">> Creating env $(ENV_NAME)"; \
		conda env create -n $(ENV_NAME) -f environment.yml; \
	fi
	@echo ">> Done. Remember to 'conda activate $(ENV_NAME)' when you want to use it."

html:
	@echo ">> Building MyST site (HTML only)…"
	myst build --html
	@echo ">> Open _build/html/index.html to view locally."

clean:
	@echo ">> Cleaning generated folders…"
	rm -rf _build figures audio
	mkdir -p figures audio
	@echo ">> Clean complete."