import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from modules.CoordinateTransformation import load_data_3body_rot as load_data

# Load data
filename = 'JanusEpimetheus-2.0'

year = 60*24*365
years = 6
data = load_data(filename)[:years*year]
n_data = len(data)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Plot
ax.scatter(data['x1'], data['y1'], label='Saturn', c='r')
ax.plot(data['x2'], data['y2'], label='Janus', c='b')
ax.plot(data['x3'], data['y3'], label='Epimetheus', c='g')

# Details
ax.axis('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Save
fig.savefig(f'{filename}_{years}year.png')
