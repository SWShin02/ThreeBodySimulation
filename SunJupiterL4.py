import numpy as np
import pandas as pd
import scipy.constants as const
from modules.CoordinateTransformation import rotate, CM
from modules.NbodySimulation import RK4

# Constants
M_sun = 1.989e30 # [kg]
G = (const.G * const.day**2 / const.au**3) * M_sun # [AU^3 day^-2 M_sun^-1]

# M_earth = 5.972e24/M_sun    # [M_sun]
M_Jupiter = 1.898e27/M_sun  # [M_sun]

r_Jupiter = 5.2 # [AU]

# Initial conditions
m = np.array([1e-2, 1e-2, 1e-3])

r_vec = np.array([[0, 0], [r_Jupiter, 0], [0, 0]])
r_vec[2] = rotate(np.pi/3, r_vec[1])
r_vec = r_vec - CM(m, r_vec)

a = r_Jupiter
w = np.sqrt(G * m.sum() / a**3)

v_vec = np.zeros((3, 2))
angular_peturbation = 0
for i in range(3):
    v_vec[i] = rotate(np.pi/2, r_vec[i]) * w
    v_vec[i] = rotate(angular_peturbation, v_vec[i])
v_vec[2] = v_vec[2]*1.02

# Simulation parameters
dt = 2 # [day]
iterations = 100000

# Dataframe
data = pd.DataFrame({
    'x1': np.zeros(iterations),
    'y1': np.zeros(iterations),
    'x2': np.zeros(iterations),
    'y2': np.zeros(iterations),
    'x3': np.zeros(iterations),
    'y3': np.zeros(iterations),
    'theta': np.zeros(iterations)
})

# Simulation
theta = 0
for i in range(iterations):
    r_vec, v_vec = RK4(m, r_vec, v_vec, dt, Gravity_constant=G)
    theta = (theta + w*dt) % (2*np.pi)
    data.loc[i] = np.array([r_vec[0, 0], r_vec[0, 1], r_vec[1, 0], r_vec[1, 1], r_vec[2, 0], r_vec[2, 1], theta])

data.to_csv('./data/SunJupiterL4.csv', index=False)
