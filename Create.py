import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def create_grid(n_rows, n_cols, size=1):
    """
    Creates a 2D grid of squares.

    Parameters:
    - n_rows: The number of rows in the grid.
    - n_cols: The number of columns in the grid.
    - size: The size of each square in the grid. Default is 1.

    Returns:
    - A tuple containing the x and y coordinates of each square in the grid.
    """
    x, y = np.meshgrid(range(n_cols), range(n_rows))
    x = x.flatten() * size
    y = y.flatten() * size
    return x, y


def create_sphere(radius=1, n_phi=30, n_theta=30):
    """
    Creates a 3D sphere.

    Parameters:
    - radius: The radius of the sphere. Default is 1.
    - n_phi: The number of divisions in the phi direction. Default is 30.
    - n_theta: The number of divisions in the theta direction. Default is 30.

    Returns:
    - A tuple containing the x, y, and z coordinates of each point on the sphere.
    """
    phi = np.linspace(0, np.pi, n_phi)
    theta = np.linspace(0, 2 * np.pi, n_theta)
    x = radius * np.outer(np.sin(phi), np.cos(theta))
    y = radius * np.outer(np.sin(phi), np.sin(theta))
    z = radius * np.outer(np.cos(phi), np.ones(n_theta))
    return x, y, z


def create_histogram(data, bins=10, xlabel=None, ylabel=None, title=None):
    """
    Creates a histogram of the input data.

    Parameters:
    - data: A list or numpy array of data to plot.
    - bins: The number of bins to use in the histogram. Default is 10.
    - xlabel: The label for the x-axis. Default is None.
    - ylabel: The label for the y-axis. Default is None.
    - title: The title for the plot. Default is None.

    Returns:
    - A tuple containing the x and y coordinates of each bar in the histogram.
    """
    heights, edges = np.histogram(data, bins=bins)
    x = (edges[:-1] + edges[1:]) / 2
    y = heights
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    return x, y


def create_scatter(x, y, z=None, xlabel=None, ylabel=None, zlabel=None, title=None):
    """
    Creates a scatter plot of the input data.

    Parameters:
    - x: A list or numpy array of x data to plot.
    - y: A list or numpy array of y data to plot.
    - z: A list or numpy array of z data to plot. If None, a 2D scatter plot is created. Default is None.
    - xlabel: The label for the x-axis. Default is None.
    - ylabel: The label for the y-axis. Default is None.
    - zlabel: The label for the z-axis. Only used if z is not None. Default is None.
    - title: The title for the plot. Default is None.

    Returns:
    - A tuple containing the x, y, and z coordinates of each point in the scatter plot.
    """
if z is None:
    plt.scatter(x, y)
else:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.title(title)
    plt.show()
return x, y, z
def create_rectangle(width=1, height=1, center=(0, 0), angle=0):
"""
Creates a rectangle.Parameters:
- width: The width of the rectangle. Default is 1.
- height: The height of the rectangle. Default is 1.
- center: The center of the rectangle as a tuple (x, y). Default is (0, 0).
- angle: The angle of rotation of the rectangle in degrees. Default is 0.

Returns:
- A tuple containing the x and y coordinates of each corner of the rectangle.
"""
x = np.array([-width/2, width/2, width/2, -width/2])
y = np.array([-height/2, -height/2, height/2, height/2])
c, s = np.cos(np.radians(angle)), np.sin(np.radians(angle))
R = np.array([[c, -s], [s, c]])
x, y = np.dot(R, np.array([x, y]))
x += center[0]
y += center[1]
return x, y
