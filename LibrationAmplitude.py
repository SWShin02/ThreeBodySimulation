import pandas as pd
import numpy as np
from modules.CoordinateTransformation import load_data_3body_rot as load_data

# Load data
info = '2.0-50'
years = 6
filename = f'JanusEpimetheus-{info}_{years}year'
print('Loading data...')
data = load_data(filename, update=False)
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
