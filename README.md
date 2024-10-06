# conftest-plugins

## build pip-requirements plugin
```
cd pip-requirements
pip install -r src/requirements.txt --target src
python3 -m zipapp src -o pip-requirements-conftest -p '/usr/bin/env python3' -c
```
