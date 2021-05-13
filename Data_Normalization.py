#away for a while
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
from sklearn.preprocessing import MinMaxScaler

def data_encoding(df):
  df1 = df.iloc[:, 1:4]
  df2 = df.iloc[:, 18:]
  df_categories = pd.concat([df1, df2], axis =1)
  df_ranges = df.iloc[:, 5:17]
  
  df_categories_encoder = pd.get_dummies(df_categories)
  df = pd.concat([df_categories_encoder, df_ranges], axis =1)
  return df

def data_normalization(df):
  scaler = MinMaxScaler()
  df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
  return df
  
df = pd.read_csv("WID3006 ML Questionnaire.csv")
df = data_encoding(df)
df_norm = data_normalization(df)
df_norm
