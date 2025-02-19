import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from modules.CoordinateTransformation import innertial_to_rotating_frame_3body as rotate_df

# Load data
info = '2.0-50'
filename = 'JanusEpimetheus-'+info

year = 60*24*365 # [minutes]
years = 6
data = pd.read_csv(f'./data/{filename}.csv', header=0)[:years*year]
data = rotate_df(data)
data.to_csv(f'./data/{filename}_{years}year_rot.csv', index=False)
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
