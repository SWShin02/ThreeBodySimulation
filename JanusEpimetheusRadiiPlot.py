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

# Binning
t_min, t_max = 0, 10 # [years], matches plotted x-range
n_bins = 40

mask = (time >= t_min) & (time <= t_max)
time_masked = time[mask]
r_Janus_masked = r_Janus[mask]
r_Epimetheus_masked = r_Epimetheus[mask]

bin_edges = np.linspace(t_min, t_max, n_bins + 1)
bin_idx = np.clip(np.digitize(time_masked, bin_edges) - 1, 0, n_bins - 1)
bin_time = (bin_edges[:-1] + bin_edges[1:]) / 2

def bin_stats(values):
    mean = np.array([values[bin_idx == i].mean() for i in range(n_bins)])
    std = np.array([values[bin_idx == i].std() for i in range(n_bins)])
    return mean, std

r_Janus_mean, r_Janus_std = bin_stats(r_Janus_masked)
r_Epimetheus_mean, r_Epimetheus_std = bin_stats(r_Epimetheus_masked)

# Layout
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

# Plot
ax.errorbar(bin_time, r_Janus_mean, yerr=r_Janus_std, label='Janus',
            fmt='s', mfc='none', color='tab:blue', capsize=3, linestyle='none')
ax.errorbar(bin_time, r_Epimetheus_mean, yerr=r_Epimetheus_std, label='Epimetheus',
            fmt='^', mfc='none', color='tab:orange', capsize=3, linestyle='none')

# Details
ax.legend(loc='upper right')
ax.set_xlabel('time [years]')
ax.set_ylabel('orbital radius [km]')
ax.set_xlim(0, 10)

ax.tick_params(axis='both', direction='in')

fig.tight_layout()

# Output
fig.savefig(f'./figures/JanusEpimetheusRadii-{group_name}.png', dpi=300)
