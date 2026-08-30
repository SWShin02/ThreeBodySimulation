import time
import h5py
import numpy as np

# HDF5 run storage
#
# Each simulation run is written to a fixed file (e.g. ./data/JanusEpimetheus.h5)
# under a group named by the run's start time (yyyymmddhhmm), so re-running a
# script accumulates runs in the same file instead of overwriting them.
#   /<yyyymmddhhmm>/innertial   (t, n_body, dim)  position in the inertial frame
#   /<yyyymmddhhmm>/theta       (t,)              mean-motion frame angle

def save_run(filepath:str, innertial:np.ndarray, theta:np.ndarray, group_name:str=None)->str:
    if group_name is None:
        group_name = time.strftime('%Y%m%d%H%M')
    with h5py.File(filepath, 'a') as f:
        group = f.create_group(group_name)
        group.create_dataset('innertial', data=innertial)
        group.create_dataset('theta', data=theta)
    return group_name

def latest_group(filepath:str)->str:
    with h5py.File(filepath, 'r') as f:
        return max(f.keys())

def load_run(filepath:str, group_name:str=None):
    with h5py.File(filepath, 'r') as f:
        if group_name is None:
            group_name = max(f.keys())
        group = f[group_name]
        innertial = group['innertial'][:]
        theta = group['theta'][:]
    return innertial, theta, group_name
