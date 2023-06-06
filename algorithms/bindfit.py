def main(
    data,
    params,
    options,
    **kwargs,
):
    import numpy as np
    import pandas as pd

    import bindfit


    # Convert params to Bindfit format
    # TODO: Modify library to accept Frictionless params format
    bindfit_params = {}

    for key, param in params["data"].items():
        bindfit_params.update({
            key: {
                "init": param["value"],
                "bounds": {
                    "min": param["lowerBound"],
                    "max": param["upperBound"],
                },
            }
        })

    # Bindfit options
    model = options["data"]["model"]
    method = options["data"]["method"]
    normalise = options["data"]["normalise"]
    dilute = options["data"]["dilute"]
    flavour = options["data"]["flavour"]

    # Load data
    df = pd.DataFrame.from_dict(data["data"])
    # Bindfit expects each variable as rows
    data_x = np.transpose(df.iloc[:, :2].to_numpy())
    data_y = np.transpose(df.iloc[:, 2:].to_numpy())

    # Apply dilution correction
    # TODO: Think about where this should go - fitter or function?
    # Or just apply it before the fit?
    if dilute:
        data_y = bindfit.helpers.dilute(data_x[0], data_y)

    function = bindfit.functions.construct(
        model,
        normalise=normalise,
        flavour=flavour,
    )

    fitter = bindfit.fitter.Fitter(
        data_x, data_y, function, normalise=normalise, params=bindfit_params
    )

    fitter.run_scipy(bindfit_params, method=method)

    summary = {
        "fitter": model,
        "fit": {
            "y": fitter.fit,
            "coeffs_raw": fitter.coeffs_raw,
            "coeffs": fitter.coeffs,
            "molefrac_raw": fitter.molefrac_raw,
            "molefrac": fitter.molefrac,
            "params": fitter.params,
            "n_y": np.array(fitter.fit).size,
            "n_params": len(fitter.params) + np.array(fitter.coeffs_raw).size,
        },
        "qof": {
            "residuals": fitter.residuals,
            "ssr": bindfit.helpers.ssr(fitter.residuals),
            "rms": bindfit.helpers.rms(fitter.residuals),
            "cov": bindfit.helpers.cov(data_y, fitter.residuals),
            "rms_total": bindfit.helpers.rms(fitter.residuals, total=True),
            "cov_total": bindfit.helpers.cov(data_y, fitter.residuals, total=True),
        },
        "time": fitter.time,
        "options": {
            "dilute": dilute,
            "normalise": normalise,
            "method": method,
            "flavour": flavour,
        },
    }

    return summary
