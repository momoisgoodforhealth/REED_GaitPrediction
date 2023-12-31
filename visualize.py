import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(-4 * np.pi, 4 * np.pi, 50)
y = np.linspace(-4 * np.pi, 4 * np.pi, 50)
z = x ** 2 + y ** 2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()