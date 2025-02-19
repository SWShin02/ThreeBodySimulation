import matplotlib.pyplot as plt
from modules.CoordinateTransformation import load_data_3body_rot as load_data

# Load data
filename = 'SunJupiterL4'
data = load_data(filename)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Plot
ax.scatter(data['x1'], data['y1'], label='Sun', c='r')
ax.scatter(data['x2'], data['y2'], label='Jupiter', c='b')
ax.plot(data['x3'], data['y3'], label='particle', c='g')

# Details
ax.axis('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Save
fig.savefig(f'{filename}.png')
