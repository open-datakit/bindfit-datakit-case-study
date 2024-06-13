# Bindfit datapackage for opendata.fit

Bindfit is a binding constant fitting tool designed to work with classical supramolecular titration data obtained from NMR, UV, Fluorescence and other methods.

* 🗒️ [Bindfit datapackage documentation](https://docs.opendata.fit/v/bindfit-datapackage/)
* 💻 [Bindfit Python library GitHub](https://github.com/opendatafit/bindfit)

## Development

Set up included Flake (`flake.nix`) with direnv (`.envrc`) to automatically load development environment.

Install/run pre-commit hooks:
```
pre-commit install
pre-commit run --all-files
```

Build container:
```
cd containers
./build.sh
```

Execute datapackage:
```
./test_datapackage.py
```
