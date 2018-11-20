.PHONY: edit

init-editors: .venv
	.venv/bin/pip install '.[editors]'
	ln -fs 'editors/jupyterlab.py' 'jupyterlab.py'
	while read EXT; do \
		.venv/bin/jupyter labextension install $$EXT; \
	done < editors/extensions.txt

clean-editors: ;

commit-editors: ;

edit: .venv
	.venv/bin/jupyter lab --config='jupyterlab.py'
