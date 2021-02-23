import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os 
import subprocess

# out = open('Jitter.txt', 'w')

# subprocess.call(['timeout','120','ping','8.8.8.8'], stdout = out)

# out.close()

df = pd.read_csv('Jitter.csv')

plt.plot(df.iloc[0:, -1],df.iloc[0:, 0])

plt.style.use('ggplot')

plt.grid(True)

plt.xlabel('Packet sequence number')
plt.ylabel('Delay (ms)')

plt.title("Jitter distribution using time series model")


plt.show()


