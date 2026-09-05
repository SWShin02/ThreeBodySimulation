import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

a = 6
ax.set_xlim(-a, a); ax.set_ylim(-a, a)
Sun = ax.scatter(data[0, 0, 0], data[0, 0, 1], label='Sun', c='r')
Jupiter = ax.scatter(data[0, 1, 0], data[0, 1, 1], label='Jupiter', c='b')
Particle = ax.scatter(data[0, 2, 0], data[0, 2, 1], label='particle', c='g')
ax.plot(data[:, 2, 0], data[:, 2, 1], c='g', linestyle='-', alpha=0.3)

ax.tick_params(axis='both', which='both', direction='in')
ax.legend(loc='upper right')

# 업데이트 함수 정의
frames = 500
interval = len(data)//frames
def update(frame:int):
    data_idx = frame*interval
    Sun.set_offsets([data[data_idx, 0]])
    Jupiter.set_offsets([data[data_idx, 1]])
    Particle.set_offsets([data[data_idx, 2]])
    return Sun, Jupiter, Particle

fig.tight_layout()

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# MP4로 저장 (ffmpeg 필요)
ani.save(f'./figures/SunJupiter-{group_name}.mp4', writer='ffmpeg', fps=30)
