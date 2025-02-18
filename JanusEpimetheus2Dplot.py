import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from modules.CoordinateTransformation import rotate

# Load data
filename = 'JanusEpimetheus-2.0'

year = 60*24*365
years = 6
data = pd.read_csv(f'./data/{filename}.csv', header=0)[:years*year]
n_data = len(data)

# Rotate
print("Data loaded. Start rotating frame")
for i in range(n_data):
    data.loc[i, ['x1', 'y1']] = rotate(r=np.array([data.loc[i, ['x1', 'y1']]][0]), theta=-data.loc[i, 'theta'])
    data.loc[i, ['x2', 'y2']] = rotate(r=np.array([data.loc[i, ['x2', 'y2']]][0]), theta=-data.loc[i, 'theta'])
    data.loc[i, ['x3', 'y3']] = rotate(r=np.array([data.loc[i, ['x3', 'y3']]][0]), theta=-data.loc[i, 'theta'])

data.to_csv(f'./data/{filename}_{years}year_rot.csv', index=False)
print('Finished')

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