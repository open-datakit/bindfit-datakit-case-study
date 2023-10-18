def main(
    datapackage,
    params,
    options,
    data,
    outputs,
    **kwargs,
):
    import bindfit

    if not data["data"]:
        raise ValueError("No data passed to algorithm")

    outputs.update(bindfit.datapackage.fit(datapackage))

    return outputs
