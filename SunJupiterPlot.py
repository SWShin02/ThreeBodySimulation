import matplotlib.pyplot as plt
from modules.CoordinateTransformation import load_data_3body_rot

plt.rcParams.update({"mathtext.fontset": "cm"})

# Load data
filepath = './data/SunJupiter.h5'
group_name = None # None = latest run
data, group_name = load_data_3body_rot(filepath, group_name)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.set_aspect('equal')

# Plot
ax.scatter(data[:, 0, 0], data[:, 0, 1], label='Sun', c='r')
ax.scatter(data[:, 1, 0], data[:, 1, 1], label='Jupiter', c='b')
ax.plot(data[:, 2, 0], data[:, 2, 1], label='particle', c='g', linestyle='-')

# Details
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.tick_params(axis='both', which='both', direction='in')
ax.legend(loc='upper right')

# Save
fig.tight_layout()
fig.savefig(f'./figures/SunJupiter-{group_name}.png', dpi=300, bbox_inches='tight')
