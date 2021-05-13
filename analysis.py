import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def multivariate(df):
    for i in range(len(df)):
        for hobby in df.loc[i,'What are your hobbies? (You may select more than 1)']:
            df.loc[i,hobby]=1
    df=df.fillna(0)
    #plot heat map
    f, ax = plt.subplots(figsize=(20, 20))
    g=sns.heatmap(df.corr().round(2),annot=True,cmap="RdYlGn")
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    return df
