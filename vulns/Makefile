.PHONY: vuln

init-vulns: .venv
	.venv/bin/pip install '.[vulns]'

clean-vulns: ;

commit-vulns: vuln;

vuln: .venv
	.venv/bin/safety check
