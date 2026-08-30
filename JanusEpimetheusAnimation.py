import matplotlib.pyplot as plt
import matplotlib.animation as animation
from modules.CoordinateTransformation import load_data_3body_rot

# Load data
filepath = './data/JanusEpimetheus.h5'
group_name = None # None = latest run
data, group_name = load_data_3body_rot(filepath, group_name)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.axis('equal')

a = 160000
ax.set_xlim(-a, a); ax.set_ylim(-a, a)
ax.scatter(0, 0, label='Saturn', c='r')
Janus = ax.scatter(data[0, 1, 0], data[0, 1, 1], label='Janus', c='b')
Epimetheus = ax.scatter(data[0, 2, 0], data[0, 2, 1], label='Epimetheus', c='g')
ax.plot(data[:, 1, 0], data[:, 1, 1], c='b', alpha=0.3)
ax.plot(data[:, 2, 0], data[:, 2, 1], c='g', alpha=0.3)

frames = 200
interval = len(data)//frames
# 업데이트 함수 정의
def update(frame:int):
    data_idx = frame*interval
    Janus.set_offsets([data[data_idx, 1]])
    Epimetheus.set_offsets([data[data_idx, 2]])
    return Janus, Epimetheus

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# GIF로 저장
ani.save(f'./figures/JanusEpimetheus-{group_name}.gif', writer='pillow')
