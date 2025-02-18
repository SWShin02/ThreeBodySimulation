import numpy as np
import pandas as pd

# Coordinate transformation
def rotate(theta, r):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) @ r

def CM(m, r_vec):
    return np.sum(m[:, np.newaxis] * r_vec, axis=0) / np.sum(m)

def innertial_to_rotating_frame_3body(df:pd.DataFrame)->pd.DataFrame:
    for i in range(len(df)):
        df.loc[i, ['x1', 'y1']] = rotate(r=np.array([df.loc[i, ['x1', 'y1']]])[0], theta=-df.loc[i, 'theta']).flatten()
        df.loc[i, ['x2', 'y2']] = rotate(r=np.array([df.loc[i, ['x2', 'y2']]])[0], theta=-df.loc[i, 'theta']).flatten()
        df.loc[i, ['x3', 'y3']] = rotate(r=np.array([df.loc[i, ['x3', 'y3']]])[0], theta=-df.loc[i, 'theta']).flatten()
    return df

def load_data_3body_rot(filename:str, update:bool=True)->pd.DataFrame:
    if update:
        df = pd.read_csv(f'./data/{filename}.csv')
        print('Creating rotating frame...')
        df = innertial_to_rotating_frame_3body(df)
        df.to_csv(f'./data/{filename}_rot.csv', index=False)
    else:
        try:
            df = pd.read_csv(f'./data/{filename}_rot.csv')
        except:
            df = pd.read_csv(f'./data/{filename}.csv')
            print('Rotating frame not found. Creating rotating frame...')
            df = innertial_to_rotating_frame_3body(df)
            df.to_csv(f'./data/{filename}_rot.csv', index=False)
    return df