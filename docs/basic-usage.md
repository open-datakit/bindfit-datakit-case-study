# Basic usage

## Upload data file

Click the "Upload new file" box at the top left of the control panel. Use the file browser to find and select the data file you want to fit. Accepted extensions are `.csv` and `.xlsx`.

A plot of your input data should appear in the right hand pane if it has been successfully uploaded.

See [here](input-data-file-formats.md) for more details on accepted input file formats.

## Select fit model

See [here](models.md) for details on available models.

## Set initial parameter values

If the fit fails or is bad, try changing the initial parameter guesses here - for example, try setting them a value lower or higher by 10 or 100.

Set minimum and maximum values in "Bounds" to constrain the search space when using a fit method other than Nelder-Mead.

## Select fit options

If unsure, you can leave these set to the default values. See [here](options.md) for more details on fit options.

## Run fit

Run the fit by clicking "Run" at the bottom right of the control panel.

If the fit fails, first to change your initial parameter guesses by a factor of 10-100 (downwards often works best). Check if the input data plots ok and looks ok.
