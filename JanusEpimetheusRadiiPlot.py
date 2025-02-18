import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.constants as const

# Load data
info = '2.0-100'
filename = 'JanusEpimetheus-'+info

data = pd.read_csv(f'./data/{filename}.csv', header=0)
r_Janus, r_Epimetheus = data['r_Janus'], data['r_Epimetheus']
n_data = len(data)

year = const.year/60
time = np.linspace(0, n_data, n_data)/year

# Layout
fig = plt.figure()
ax = fig.add_subplot()

# Plot
ax.plot(time, r_Janus, label='Janus')
ax.plot(time, r_Epimetheus, label='Epimetheus')

# Details
ax.legend(loc='upper right')
ax.set_xlabel('time [years]')
ax.set_ylabel('orbital radius [km]')
ax.set_xlim(0, 10)

fig.tight_layout()

# Output
fig.savefig(f'JanusEpimetheusRadii-{info}.png')