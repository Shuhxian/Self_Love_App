import sys 
sys.path.append("../")
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
from sklearn.preprocessing import MinMaxScaler

def data_encoding(df):
    df1 = df.iloc[:, 1:3]
    df2 = df.iloc[:, 18:]
    df_categories = pd.concat([df1, df2], axis =1)
    df_hobby=df.iloc[:,3]
    df_ranges = df.iloc[:, 4:18]
  
    #df_categories_encoder = df_categories.apply(LabelEncoder().fit_transform)
    df_categories_encoder = pd.get_dummies(df_categories, drop_first = True)
    df = pd.concat([df_categories_encoder, df_ranges], axis =1)
    df = pd.concat([df, df_hobby], axis =1)
    for i in range(len(df)):
        for hobby in df.loc[i,'What are your hobbies? (You may select more than 1)']:
            df.loc[i,hobby]=1
    df=df.fillna(0)
    del df['What are your hobbies? (You may select more than 1)']
    return df

def label_encoding(df):
    df1 = df.iloc[:, 1:3]
    df2 = df.iloc[:, 18:]
    df_categories = pd.concat([df1, df2], axis =1)
    df_hobby=df.iloc[:,3].to_frame()
    df_ranges = df.iloc[:, 4:18]
    
    df_categories_encoder = df_categories.apply(LabelEncoder().fit_transform)
    x_df = pd.concat([df_categories_encoder, df_ranges], axis =1)

    for i in range(len(df_hobby)):
        for hobby in df_hobby.loc[i,'What are your hobbies? (You may select more than 1)']:
            df_hobby.loc[i,hobby]=1
    y_df = df_hobby.fillna(0)
    del y_df['What are your hobbies? (You may select more than 1)']
    return x_df, y_df

def data_normalization(df):
  # explicity min max scale because we already know the range is from 5 to 1
  df.iloc[:,50:64] = df.iloc[:,50:64].apply(lambda x: (x-1)/(5-1)) 
  return df

if __name__ == "__main__":
    df = pd.read_csv("WID3006 ML Questionnaire.csv")
    df = data_encoding(df)
    df_norm = data_normalization(df)
    #df_norm.corr(method='pearson')
    df_norm

#Multicollinearity Checking
'''
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calc_vif(X):

    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    return(vif)

calc_vif(df_norm)
'''
