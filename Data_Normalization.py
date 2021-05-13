import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
from sklearn.preprocessing import MinMaxScaler

def data_encoding(df):
    df1 = df.iloc[:, 1:3]
    df2 = df.iloc[:, 18:]
    df_categories = pd.concat([df1, df2], axis =1)
    df_ranges = df.iloc[:, 3:17]
  
    df_categories_encoder = df_categories.apply(LabelEncoder().fit_transform)
    df = pd.concat([df_categories_encoder, df_ranges], axis =1)
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.split(";")
    for i in range(len(df)):
        for hobby in df.loc[i,'What are your hobbies? (You may select more than 1)']:
            df.loc[i,hobby]=1
    df=df.fillna(0)
    del df['What are your hobbies? (You may select more than 1)']
    return df

def data_normalization(df):
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df
  
df = pd.read_csv("WID3006 ML Questionnaire.csv")
df = data_encoding(df)
df_norm = data_normalization(df)
df_norm
