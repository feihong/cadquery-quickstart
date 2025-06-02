# You need to get this manually if you're not using a virtualenv
scripts_path := `python -c 'import sysconfig; print(sysconfig.get_path("scripts"))'`

install:
	pip install -r requirements.txt

edit file:
    {{scripts_path}}/CQ-Editor {{file}}
