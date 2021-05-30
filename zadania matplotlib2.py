import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
'''
# zad 1
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.linspace(0, 2*np.pi, 100)
z = t
x = np.sin(t)
y = np.cos(t)*2
ax.plot(x, y, z, label='zadanie 1')
ax.legend()
plt.show()
'''
'''
# zad 2

np.random.seed(19680801)


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
for c, m, zlow, zhigh in [('r', 'o', 23, -7), ('b', '^', 20, -5), ('g', 'd', 20, -5), ('y', 'X', 10, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    ys1 = randrange(n, 90, 100)
    ys2 = randrange(n, 50, 70)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, ys1, ys2, zs, c=c, marker=m)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
'''
# zad3
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
my_col = cm.jet(Z/np.amax(Z))
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors = my_col,
        linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
plt.show()