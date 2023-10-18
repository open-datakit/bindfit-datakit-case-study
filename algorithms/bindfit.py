def main(
    datapackage,
    params,
    options,
    data,
    outputs,
    **kwargs,
):
    import bindfit

    outputs.update(bindfit.datapackage.fit(datapackage))

    return outputs
