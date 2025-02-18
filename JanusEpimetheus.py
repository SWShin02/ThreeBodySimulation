import numpy as np
import pandas as pd
import scipy.constants as const
from modules.CoordinateTransformation import CM
from modules.NbodySimulation import RK4

# Constants
M_Saturn = 5.6834e26 # kg
M_Janus = 1.894e18 # kg
M_Epimetheus = 5.256e17 # kg

Delta_r = 50
r_Janus = 151460 # km
r_Epimetheus = r_Janus - Delta_r # km
r0 = (M_Janus*r_Janus + M_Epimetheus*r_Epimetheus) / (M_Janus + M_Epimetheus)


G = const.G / const.kilo**3 # km^3 sec^-2 kg^-1
year = int(const.year)

# Mass
m = np.array([M_Saturn, M_Janus, M_Epimetheus])

# Initial location
r_vec = np.array([[0, 0], [r_Janus, 0], [-(r_Epimetheus), 0]])
r_vec = r_vec - CM(m, r_vec)

# Initial velocity
v_vec = np.zeros((3, 2))
v_vec[1][1] = np.sqrt(G*M_Saturn/r_Janus)
v_vec[2][1] = -np.sqrt(G*M_Saturn/r_Epimetheus)
v_vec[0][1] = -(m[1]*v_vec[1][0] + m[2]*v_vec[2][0])/m[0]

w = np.sqrt(G*M_Saturn/r0**3)

# Simulation parameters
dt = 1 # second
iterations = year*20 # 20 years
n_data = iterations // 60 # every minutes

# Dataframe
data = pd.DataFrame({
    'x1': np.zeros(n_data),
    'y1': np.zeros(n_data),
    'x2': np.zeros(n_data),
    'y2': np.zeros(n_data),
    'x3': np.zeros(n_data),
    'y3': np.zeros(n_data),
    'theta': np.zeros(n_data),
    'r_Janus': np.zeros(n_data),
    'r_Epimetheus': np.zeros(n_data)
})


# Simulation
print('Simulation starts')
theta = 0
twopi = 2*np.pi
for i in range(iterations):
    r_vec, v_vec = RK4(m, r_vec, v_vec, dt, Gravity_constant=G)
    theta = (theta + w*dt) % (twopi)
    if i % 60 == 0: # every minutes
        data.loc[i//60] = np.array([
            r_vec[0, 0], r_vec[0, 1], 
            r_vec[1, 0], r_vec[1, 1], 
            r_vec[2, 0], r_vec[2, 1],
            theta,
            np.linalg.norm(r_vec[1]),
            np.linalg.norm(r_vec[2])
        ])
        if i % 2592000 == 0: # every month
            print(f'Progress: {i/iterations*100:.1f}%')
        if i % year == 0:
            print(f'{i//year} years')

data.to_csv(f'./data/JanusEpimetheus-{M_Janus/M_Epimetheus:.1f}-{Delta_r}.csv', index=False)
