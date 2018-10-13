.PHONY: edit

init-editors: .venv
	.venv/bin/pip install '.[editors]'
	while read EXT; do \
		.venv/bin/jupyter labextension install $$EXT; \
	done < editors/extensions.txt 

clean-editors: ;

commit-editors: ;

edit: .venv
	.venv/bin/jupyter lab --config=editors/jupyterlab.py
