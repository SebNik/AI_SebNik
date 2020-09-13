# this file is calculating the route of the race pod
import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt


def generate_map(checkpoint_count=3, boundaries=9000, radius_checkpoint=600):
    # generating the map for the game
    # creating random checkpoints
    checkpoints_coordinates = np.random.randint(100, boundaries, size=(checkpoint_count, 2))
    # start point player
    start_point = np.random.randint(100, boundaries, size=2)
    # start vector player
    start_vector = np.random.randint(100, size=2)
    # returning the values
    return checkpoints_coordinates, start_point, start_vector


def create_route(checkpoints_coordinates, start_point, start_vector):
    # this function will create the route
    x = np.r_[checkpoints_coordinates[:, 0], checkpoints_coordinates[0, 0]]
    y = np.r_[checkpoints_coordinates[:, 1], checkpoints_coordinates[0, 1]]
    # print(x, y)
    # fit splines to x=f(u) and y=g(u), treating both as periodic. also note that s=0
    # is needed in order to force the spline fit to pass through all the input points.
    tck, u = interpolate.splprep([x, y], s=0, per=True)
    # evaluate the spline fits for 1000 evenly spaced distance values
    xi, yi = interpolate.splev(np.linspace(0, 1, 50), tck)
    # creating vectors dummy
    vectors = np.array([[23, 8, 0.5, 1], [24, 11, 1, 1]])
    # retuning the generated route
    return checkpoints_coordinates, start_point, start_vector, xi, yi, vectors


def plot_data(checkpoints_coordinates, start_point, start_vector, xi, yi, vectors):
    # plotting the data
    # plot the result
    fig, ax = plt.subplots(1, 1)
    ax.plot(checkpoints_coordinates[:, 0], checkpoints_coordinates[:, 1], 'or', label='points')
    ax.plot(xi, yi, '-b', label='line')

    soa = np.array([[23, 8, 0.5, 1], [24, 11, 1, 1]])
    X, Y, U, V = zip(*soa)

    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, width=0.008, color='lawngreen')

    plt.legend()
    plt.draw()
    plt.show()


if __name__ == '__main__':
    # start code
    coor, s_p, s_v = generate_map()
    print(coor, s_p, s_v)
    # generating the route
    c_c, s_p, s_v, x, y, v = create_route(coor, s_p, s_v)
    # plotting the data
    plot_data(c_c, s_p, s_v, x, y, v)
