def multivariate(df):
    for i in range(len(df)):
        for hobby in df.loc[i,'What are your hobbies? (You may select more than 1)']:
            df.loc[i,hobby]=1
    df=df.fillna(0)
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20,20))
    #plot heat map
    g=sns.heatmap(df.corr(),annot=True,cmap="RdYlGn")
