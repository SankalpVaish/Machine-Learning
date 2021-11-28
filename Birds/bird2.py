import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
birddata=pd.read_csv("bird_tracking.csv")
ix=birddata.bird_name== "Eric"
speed=birddata.speed_2d[ix]
plt.figure(figsize=(8,4))
print(np.isnan(speed))
print(np.isnan(speed.any()))
print(np.sum(np.isnan(speed)))
ind=np.isnan(speed)
print(ind)
print(~ind)
print(plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed =True))
plt.xlabel("Speed 2D")
plt.ylabel("Frequency");
