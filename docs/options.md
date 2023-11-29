# Options

## Fit method

This sets the fit search algorithm to be used. Currently you can choose between Nelder-Mead (Simplex) and L-BFGS-B (quasi-Newtonian).

### Nelder-Mead (Simplex)

Nelder-Mead is the default and most commonly applicable option - we recommend using this unless you have a good reason to change it.

### L-BFGS-B (quasi-Newtonian)

L-BFGS-B can be used if you need to constrain the fit search space using the minimum and maximum bounds option, however is more prone to failing to find a good fit.

## Subtract initial values

Defaults to true.

When true, the fitting process assumes the first data point (second row in input file) is the chemical shift of the pure host and therefore only deals with the difference between the pure host and the complex(es).

When false, the fitting process assumes the chemical shift for the host is unknown and includes that in the fitting process (one extra parameter).

## Dilution correction

Not applicable for NMR (makes no difference) as this only applies to UV-Vis methods. Defaults to false for NMR models and true for UV models.
