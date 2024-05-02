def main(
    data,
    fitMethod,
    fitModel,
    fitModelParams,
    subInitValues,
    dilutionCorrection,
    flavour,
):
    """Construct and run a Bindfit fitter given a dataset and parameters

    Arguments
    ----------
    data: `list`
        Tabular input data in array of named row objects format
    fitMethod: `str`
        The optimisation algorithm to use for fitting
    fitModel: `str`
        The model to fit to the data
    fitModelParams: `list`
        Table of input parameters containing initial values and bounds
    subInitValues: `bool`
        If true, subtract the first column from all data before fitting
    dilutionCorrection: `bool`
        If true, apply dilution correction to data before fitting
    flavour: `str` or None
        If not None, one of "add", "stat" or "noncoop"

    Returns
    -------
    TODO
    """
    # Imports
    import numpy as np
    import bindfit
    import opendatafit

    # Error checks
    if not data["data"]:
        raise ValueError("No data passed to algorithm")

    # Munge data into Bindfit format
    # Bindfit expects each variable as rows
    df = opendatafit.helpers.tabular_data_resource_to_dataframe(data)
    data_x = np.transpose(df.iloc[:, :2].to_numpy())
    data_y = np.transpose(df.iloc[:, 2:].to_numpy())

    # Convert param initial values and bounds to Bindfit format
    input_params = {}

    for param in fitModelParams["data"]:
        input_params.update(
            {
                param["name"]: {
                    "init": param["value"],
                    "bounds": {
                        "min": param["lowerBound"],
                        "max": param["upperBound"],
                    },
                }
            }
        )

    # Apply dilution correction
    # TODO: Think about where this should go - fitter or function?
    # Or just apply it before the fit?
    if dilutionCorrection:
        data_y = bindfit.helpers.dilute(data_x[0], data_y)

    # Construct and run Bindfit fitter
    function = bindfit.functions.construct(
        fitModel,
        normalise=subInitValues,
        flavour=flavour,
    )

    fitter = bindfit.fitter.Fitter(
        data_x, data_y, function, normalise=subInitValues, params=input_params
    )

    fitter.run_scipy(input_params, method=fitMethod)

    # Munge output data

    # Optimised parameter values
    for param in fitModelParams["data"]:
        key = param["name"]
        if key in fitter.params:
            param["value"] = fitter.params[key]["value"]
            param["stderr"] = fitter.params[key]["stderr"]

    return {
        "fitModelParams": fitModelParams
    }
