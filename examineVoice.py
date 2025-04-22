import numpy as np

file = np.load("voices/Emmett.npz", allow_pickle=True)
print("Keys in Emmett.npz:", list(file.keys()))
