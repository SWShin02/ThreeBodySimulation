import h5py
import numpy as np
from numba import njit

# Coordinate transformation
def rotate(theta, r):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) @ r

def CM(m, r_vec):
    return np.sum(m[:, np.newaxis] * r_vec, axis=0) / np.sum(m)

@njit(cache=True)
def innertial_to_rotating_frame_3body(innertial:np.ndarray, theta:np.ndarray)->np.ndarray:
    """innertial: (t, n_body, 2), theta: (t,) -> rotating-frame positions (t, n_body, 2)."""
    t, n_body, _ = innertial.shape
    rotating = np.empty((t, n_body, 2))
    for i in range(t):
        c = np.cos(theta[i])
        s = np.sin(theta[i])
        for j in range(n_body):
            x = innertial[i, j, 0]
            y = innertial[i, j, 1]
            rotating[i, j, 0] = c * x + s * y
            rotating[i, j, 1] = -s * x + c * y
    return rotating

def load_data_3body_rot(filepath:str, group_name:str=None, update:bool=False):
    """Load (and cache) the rotating-frame positions for one run in an HDF5 file.

    Returns (rotating: (t, n_body, 2) ndarray, group_name). If the 'rotating'
    dataset is already cached in the run's group it is reused unless
    update=True; otherwise it is computed from 'innertial'/'theta' and stored
    back into the same group.
    """
    with h5py.File(filepath, 'a') as f:
        if group_name is None:
            group_name = max(f.keys())
        group = f[group_name]
        if 'rotating' in group and not update:
            return group['rotating'][:], group_name
        rotating = innertial_to_rotating_frame_3body(group['innertial'][:], group['theta'][:])
        if 'rotating' in group:
            del group['rotating']
        group.create_dataset('rotating', data=rotating)
    return rotating, group_name
