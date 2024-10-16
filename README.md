# Bindfit dataflow for opendata.studio

Bindfit is a binding constant fitting tool designed to work with classical supramolecular titration data obtained from NMR, UV, Fluorescence and other methods.

* 🗒️ [Bindfit dataflow documentation](https://docs.opendata.fstudio/v/bindfit-dataflow/)
* 💻 [Bindfit Python library GitHub](https://github.com/opendatastudio/bindfit)

## Example usage
```
opends reset                                   # Clear any previous outputs
opends init                                    # Initialise the default run
opends load data ./data/nmr11.csv      # Load input data
opends set model "nmr1to1"                    # Set fit model
opends set method "nelder-mead"                # Set fit method
opends set inputParams.k.init 314              # Set initial parameter guess
opends run                                     # Run algorithm
opends show outputParams                             # View optimised parameters
opends show summary                         # View fit summary
opends view fitGraphMatplotlib                 # View fit graph
```

## Development

### Requirements

* Docker
* Python (to run CLI)
* [opendatastudio/cli](https://github.com/opendatastudio/cli)
* [opendatastudio/containers](https://github.com/opendatastudio/containers)

### Set up pre-commit hooks

Set up included Flake (`flake.nix`) with direnv (`.envrc`) to automatically load development environment.

Install/run pre-commit hooks:
```
pre-commit install
pre-commit run --all-files
```

### Build execution container

Build base execution container:
```
# Navigate to opendatastudio/python-run-base repository
./build.sh
```

Build bindfit-dataflow container:
```
# Navigate back to bindfit-dataflow repository
cd containers
./build.sh
```

### Install CLI

```
python -m venv .venv
source .venv/bin/activate
pip install -e /PATH/TO/CLI

opends  # Check CLI is installed
```

See [Usage](#usage) for command reference.
