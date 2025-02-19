import matplotlib.pyplot as plt
import matplotlib.animation as animation
from modules.CoordinateTransformation import load_data_3body_rot as load_data

# Load data
filename = 'JanusEpimetheus-2.0_6year'
data = load_data(filename, update=False)

# Layout
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.axis('equal')

a = 160000
ax.set_xlim(-a, a); ax.set_ylim(-a, a)
ax.scatter(0, 0, label='Saturn', c='r')
Janus = ax.scatter(data.loc[0, 'x2'], data.loc[0, 'y2'], label='Janus', c='b')
Epimetheus = ax.scatter(data.loc[0, 'x3'], data.loc[0, 'y3'], label='Epimetheus', c='g')
ax.plot(data['x2'], data['y2'], c='b', alpha=0.3)
ax.plot(data['x3'], data['y3'], c='g', alpha=0.3)

frames=200
interval = len(data)//frames
# 업데이트 함수 정의
def update(frame:int):
    data_idx = frame*interval
    Janus.set_offsets([[data.loc[data_idx, 'x2'], data.loc[data_idx, 'y2']]])
    Epimetheus.set_offsets([[data.loc[data_idx, 'x3'], data.loc[data_idx, 'y3']]])
    return Janus, Epimetheus

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# GIF로 저장
ani.save('./figures/JanusEpimetheus.gif', writer='pillow')
