import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = 'results/RES_1.csv'
df = pd.read_csv(filename)

# Graph 1
t = 60
o = 1

df_1 = df.loc[(df['t'] == t) & (df['o'] == o)]

print(df_1)