import numpy as np
from modules.DataIO import load_run

# Load data
print('Loading data...')
filepath = './data/JanusEpimetheus.h5'
group_name = None # None = latest run
innertial, theta, group_name = load_run(filepath, group_name)
n_data = len(innertial)
print('Finished')

# Compute Radius Amplitude
year = 60*24*365 # [minutes]
r_Janus = np.linalg.norm(innertial[:, 1], axis=1)
r_Epimetheus = np.linalg.norm(innertial[:, 2], axis=1)

r_Janus_min = np.average(r_Janus[3*year:5*year])
r_Janus_max = np.average(r_Janus[7*year:9*year])
Amplitude_Janus = r_Janus_max - r_Janus_min

r_Epimetheus_max = np.average(r_Epimetheus[3*year:5*year])
r_Epimetheus_min = np.average(r_Epimetheus[7*year:9*year])
Amplitude_Epimetheus = r_Epimetheus_max - r_Epimetheus_min

print(f'Janus amplitude: {Amplitude_Janus:.1f}')
print(f'Epimetheus amplitude: {Amplitude_Epimetheus:.1f}')
print(f'Amplitude ratio: 1 : {Amplitude_Epimetheus/Amplitude_Janus:.1f}')
