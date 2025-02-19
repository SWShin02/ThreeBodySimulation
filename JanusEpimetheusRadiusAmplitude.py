import pandas as pd
import numpy as np

# Load data
print('Loading data...')
filename = 'JanusEpimetheus-2.0'
data = pd.read_csv(f'./data/{filename}.csv')
n_data = len(data)
print('Finished')

# Compute Radius Amplitude
year = 60*24*365 # [minutes]
r_Janus, r_Epimetheus = data['r_Janus'], data['r_Epimetheus']

r_Janus_min = np.average(r_Janus[3*year:5*year])
r_Janus_max = np.average(r_Janus[7*year:9*year])
Amplitude_Janus = r_Janus_max - r_Janus_min

r_Epimetheus_max = np.average(r_Epimetheus[3*year:5*year])
r_Epimetheus_min = np.average(r_Epimetheus[7*year:9*year])
Amplitude_Epimetheus = r_Epimetheus_max - r_Epimetheus_min

print(f'Janus amplitude: {Amplitude_Janus:.1f}')
print(f'Epimetheus amplitude: {Amplitude_Epimetheus:.1f}')
print(f'Amplitude ratio: 1 : {Amplitude_Epimetheus/Amplitude_Janus:.1f}')
