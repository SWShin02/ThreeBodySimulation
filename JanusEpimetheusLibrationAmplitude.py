import numpy as np
from modules.CoordinateTransformation import load_data_3body_rot

# Load data
filepath = './data/JanusEpimetheus.h5'
group_name = None # None = latest run
years = 6
minute = 60*24*365 # [minutes] per year, data recorded every minute

print('Loading data...')
data, group_name = load_data_3body_rot(filepath, group_name)
data = data[:years*minute]
n_data = len(data)
print('Finished')

# Compute angular location in rotating frame
# Janus
x_Janus, y_Janus = data[:, 1, 0], data[:, 1, 1]
theta_Janus = np.arctan2(y_Janus, x_Janus)
amplitude_Janus = theta_Janus.max() - theta_Janus.min()
amplitude_Janus = np.rad2deg(amplitude_Janus)

# Epimetheus
x_Epimetheus, y_Epimetheus = data[:, 2, 0], data[:, 2, 1]
theta_Epimetheus = np.arctan2(y_Epimetheus, x_Epimetheus)
UHP = y_Epimetheus >= 0
LHP = y_Epimetheus < 0
amplitude_Epimetheus = 2*np.pi - (theta_Epimetheus[UHP].min() - theta_Epimetheus[LHP].max())
amplitude_Epimetheus = np.rad2deg(amplitude_Epimetheus)

print(f'Janus amplitude: {amplitude_Janus:.1f} deg')
print(f'Epimetheus amplitude: {amplitude_Epimetheus:.1f} deg')
print(f'Amplitude ratio: 1 : {amplitude_Epimetheus/amplitude_Janus:.1f}')
