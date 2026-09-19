.PHONY: install test compile clean

install:
	python -m pip install -r requirements-dev.txt

test:
	python -m pytest

compile:
	python -m compileall -q src

clean:
	python -c "import shutil; from pathlib import Path; [shutil.rmtree(p, ignore_errors=True) for p in Path('.').rglob('__pycache__')]"
