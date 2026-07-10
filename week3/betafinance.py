import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AMZN.csv")
df2 = pd.read_csv("PG.csv")

temp = df["Return"] - df["Return"].mean()
temp2 = df2["Return"] - df2["Return"].mean()

covar = (temp * temp2).sum()/(len(df)-1)

variance = (((df2["Return"] - df2["Return"].mean()) ** 2).sum()) / len(df2)

beta = covar / variance
print("Beta coefficient is:", beta)