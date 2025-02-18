import pandas as pd
import numpy as np

# Load data
print('Loading data...')
filename = 'JanusEpimetheus-2.0'
years = 6
data = pd.read_csv(f'./data/{filename}_{years}year_rot.csv')
n_data = len(data)
print('Finished')

# Compute angular location in rotating frame
# Janus
theta_Janus = np.arctan2(data['y2'], data['x2'])
amplitude_Janus = theta_Janus.max() - theta_Janus.min()
amplitude_Janus = np.rad2deg(amplitude_Janus)

# Epimetheus
theta_Epimetheus = np.arctan2(data['y3'], data['x3'])
UHP = data['y3'] >= 0
LHP = data['y3'] < 0
amplitude_Epimetheus = 2*np.pi - (theta_Epimetheus[UHP].min() - theta_Epimetheus[LHP].max())
amplitude_Epimetheus = np.rad2deg(amplitude_Epimetheus)

print(f'Janus amplitude: {amplitude_Janus:.1f} deg')
print(f'Epimetheus amplitude: {amplitude_Epimetheus:.1f} deg')
print(f'Amplitude ratio: 1 : {amplitude_Epimetheus/amplitude_Janus:.1f}')