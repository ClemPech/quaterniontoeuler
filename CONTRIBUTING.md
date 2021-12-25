# Contributing
```sh
pip install -U -r requirements/dev.txt
```

#### venv
better use `venv` when contributing
For example on linux
```sh
python3 -m venv .venv
sudo .venv/bin/activate
```
## Contributing to docs

### build README.md

This will erase the previous README.md file

use https://pypi.org/project/sphinx-markdown-builder/ to build the README.md from the docs.
install with pip

```sh
pip install sphinx-markdown-builder
make readmeMD
```

