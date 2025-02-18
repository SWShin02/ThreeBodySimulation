import numpy as np
import scipy.constants as const

def compute_gravitational_field(m, r_vec, N_body:int, Gravity_constant:float=const.G):
    g = np.zeros((N_body, 2))
    for i in range(N_body):
        for j in range(N_body):
            if i != j:
                r = r_vec[j] - r_vec[i]
                g[i] += Gravity_constant * m[j] * r / np.linalg.norm(r)**3
    return g 

def RK4(m, r_vec:np.ndarray, v_vec:np.ndarray, dt:float, 
        N_body:int=3, Gravity_constant:float=const.G)->np.ndarray:
    k1_v = compute_gravitational_field(m, r_vec, 
        N_body=N_body, Gravity_constant=Gravity_constant)*dt
    k1_r = v_vec*dt

    k2_v = compute_gravitational_field(m, r_vec + k1_r/2, 
        N_body=N_body, Gravity_constant=Gravity_constant)*dt
    k2_r = (v_vec + k1_v/2)*dt

    k3_v = compute_gravitational_field(m, r_vec + k2_r/2, 
        N_body=N_body, Gravity_constant=Gravity_constant)*dt
    k3_r = (v_vec + k2_v/2)*dt

    k4_v = compute_gravitational_field(m, r_vec + k3_r, 
        N_body=N_body, Gravity_constant=Gravity_constant)*dt
    k4_r = (v_vec + k3_v)*dt

    r_vec = r_vec + (k1_r + 2*k2_r + 2*k3_r + k4_r)/6
    v_vec = v_vec + (k1_v + 2*k2_v + 2*k3_v + k4_v)/6   

    return r_vec, v_vec