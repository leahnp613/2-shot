push_all:
	git push github && git push origin

format:
	black . && djlint . --reformat

venv:
	source .venv/bin/activate