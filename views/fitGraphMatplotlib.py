import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.optimize import curve_fit


def main(
    data: pd.DataFrame, fitCurve: pd.DataFrame, fitResiduals: pd.DataFrame
) -> Figure:
    # Data
    x = np.arange(1, 10, 0.2)
    ynoise = x * np.random.rand(len(x))
    ydata = x**2 + ynoise

    Fofx = lambda x, a, b, c: a * x**2 + b * x + c  # noqa: E731
    p, cov = curve_fit(Fofx, x, ydata)

    # Upper plot
    fig1 = plt.figure(1)
    frame1 = fig1.add_axes((0.1, 0.3, 0.8, 0.6))

    plt.plot(x, ydata, ".b")
    plt.plot(x, Fofx(x, *p), "-r")

    frame1.set_xticklabels([])
    plt.grid()

    # Residual plot
    difference = Fofx(x, *p) - ydata
    fig1.add_axes((0.1, 0.1, 0.8, 0.2))
    plt.plot(x, difference, "or")
    plt.grid()

    # Return current figure
    return plt.gcf()
