import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def multivariate(df):
    #Plot heat map
    f, ax = plt.subplots(figsize=(30, 30))
    g=sns.heatmap(df.corr(),fmt='.2f',annot=True,cmap="RdYlGn")
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    return df
