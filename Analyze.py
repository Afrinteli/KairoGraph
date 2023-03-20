import pandas as pd
import matplotlib.pyplot as plt


def plot_histogram(data, bins=10, xlabel=None, ylabel=None, title=None):
    """
    Plots a histogram of the input data.

    Parameters:
    - data: A list or numpy array of data to plot.
    - bins: The number of bins to use in the histogram. Default is 10.
    - xlabel: The label for the x-axis. Default is None.
    - ylabel: The label for the y-axis. Default is None.
    - title: The title for the plot. Default is None.
    """
    plt.hist(data, bins=bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_scatter(x, y, xlabel=None, ylabel=None, title=None):
    """
    Plots a scatter plot of the input data.

    Parameters:
    - x: A list or numpy array of x data to plot.
    - y: A list or numpy array of y data to plot.
    - xlabel: The label for the x-axis. Default is None.
    - ylabel: The label for the y-axis. Default is None.
    - title: The title for the plot. Default is None.
    """
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def analyze_table(filename):
    """
    Analyzes a table from a CSV file.

    Parameters:
    - filename: The name of the CSV file to analyze.

    Returns:
    - A Pandas DataFrame object representing the table data.
    """
    data = pd.read_csv(filename)
    summary = data.describe()
    return summary
