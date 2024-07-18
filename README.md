# Bindfit datapackage for opendata.fit

Bindfit is a binding constant fitting tool designed to work with classical supramolecular titration data obtained from NMR, UV, Fluorescence and other methods.

* 🗒️ [Bindfit datapackage documentation](https://docs.opendata.fit/v/bindfit-datapackage/)
* 💻 [Bindfit Python library GitHub](https://github.com/opendatafit/bindfit)

## Usage
```
opendata-cli reset  # Clear any previous outputs
opendata-cli load bindfit data ./data/nmr11.csv  # Load input data
opendata-cli set-param bindfit fitModelParams k 314  # Set initial parameter guess
opendata-cli run bindfit  # Run algorithm
opendata-cli view fitGraphMatplotlib  # View fit graph
```

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
