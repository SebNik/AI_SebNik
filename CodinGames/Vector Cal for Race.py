# this file is calculating the route of the race pod
import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt


def generate_map(checkpoint_count=3, boundaries_x=16000, boundaries_y=9000, radius_checkpoint=600):
    # generating the map for the game
    # creating random checkpoints
    x = random.randint(100, size=(3, 5))

# x = np.array([23, 23.5, 24, 25, 25, 23])
# y = np.array([8, 9, 11, 12, 13, 12])
#
# # append the starting x,y coordinates
# x = np.r_[x, x[0]]
# y = np.r_[y, y[0]]
#
# # fit splines to x=f(u) and y=g(u), treating both as periodic. also note that s=0
# # is needed in order to force the spline fit to pass through all the input points.
# tck, u = interpolate.splprep([x, y], s=0, per=True)
#
# # evaluate the spline fits for 1000 evenly spaced distance values
# xi, yi = interpolate.splev(np.linspace(0, 1, 50), tck)
#
# # plot the result
# fig, ax = plt.subplots(1, 1)
# ax.plot(x, y, 'or', label='points')
# ax.plot(xi, yi, '-b', label='line')
#
# soa = np.array([[23, 8, 0.5, 1], [24, 11, 1, 1]])
# X, Y, U, V = zip(*soa)
#
# ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, width=0.008, color='lawngreen')
#
#
# plt.legend()
# plt.draw()
# plt.show()

if __name__ == '__main__':
    None