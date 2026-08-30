import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from modules.DataIO import load_run

# Load data
filepath = './data/JanusEpimetheus.h5'
group_name = None # None = latest run

innertial, theta, group_name = load_run(filepath, group_name)
r_Janus = np.linalg.norm(innertial[:, 1], axis=1)
r_Epimetheus = np.linalg.norm(innertial[:, 2], axis=1)
n_data = len(innertial)

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
fig.savefig(f'./figures/JanusEpimetheusRadii-{group_name}.png')
