import matplotlib.pyplot as plt
import matplotlib.animation as animation
from modules.CoordinateTransformation import load_data_3body_rot as load_data

# Load data
filename = 'threebodyL4'
data = load_data(filename, update=False)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.axis('equal')

a = 6
ax.set_xlim(-a, a); ax.set_ylim(-a, a)
Sun = ax.scatter(data.loc[0, 'x1'], data.loc[0, 'y1'], label='Sun', c='r')
Jupiter = ax.scatter(data.loc[0, 'x2'], data.loc[0, 'y2'], label='Jupiter', c='b')
Particle = ax.scatter(data.loc[0, 'x3'], data.loc[0, 'y3'], label='particle', c='g')

# 업데이트 함수 정의
def update(frame:int):
    data_idx = frame*100
    Sun.set_offsets([[data.loc[data_idx, 'x1'], data.loc[data_idx, 'y1']]])
    Jupiter.set_offsets([[data.loc[data_idx, 'x2'], data.loc[data_idx, 'y2']]])
    Particle.set_offsets([[data.loc[data_idx, 'x3'], data.loc[data_idx, 'y3']]])
    return Sun, Jupiter, Particle

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=500, blit=True)

# GIF로 저장
ani.save('animation.gif', writer='pillow')
