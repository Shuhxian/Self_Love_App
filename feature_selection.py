import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.model_selection import train_test_split
from data_cleaning import *
from Data_Normalization import *

def chi2_analysis(x_train_label_encoded, x_label_encoded_df, y_train):
    """
    Perform chi-square test between each question and each hobby then return the average score of each question 
    
    """
    selected_features = [] 
    # loop over each hobby to calculate the feature scores with respect to the hobby
    for i in range(y_train.shape[1]):
        selector = SelectKBest(chi2, k='all')
        selector.fit(x_train_label_encoded, y_train[:,i])
        selected_features.append(list(selector.scores_))

    # average the feature scores by question 
    selected_features = np.mean(selected_features, axis=0) 

    # a dataframe table that show each question feature scores
    return pd.DataFrame(selected_features[:,None], index=x_label_encoded_df.columns).sort_values(0, ascending = False)

def filter_features(best_k_features, df_norm):
    """
    filter the features by questions
    """
    return df_norm[ [column_name 
                    for column_name in df_norm.columns 
                    for question in best_k_features 
                    if column_name.startswith(question)]]

def select_best_k_features(df, k=None, thres_value=None, more_than_thres_value = True ):
    """
    choose the best k features by setting a threshold or specify the number of best features 
    """
    if k:
        # choose the k best feature by explicitly stating the length
        best_k_features = df.index[:k].tolist()
    elif thres_value:
        # choose the k best feature by certain threshold
        if more_than_thres_value:
            best_k_features = df[df[0] > thres_value].index.tolist()
        else:
            best_k_features = df[df[0] < thres_value].index.tolist()
    
    return best_k_features

if __name__ == "__main__":
    # to do the chi2 analysis
    df = pd.read_csv("WID3006 ML Questionnaire.csv")
    df = data_cleaning(df)
    # label encoding is used instead of one-hot encoding because one-hot encoding will create many features for one question
    # but label encoding is able to perform chi-square test between a single question as a whole and the hobby  
    x_df, y_df = label_encoding(df)
    # only evaluate on train data to prevent data leakage
    x_train_label_encoded, _, y_train, _ = train_test_split(x_df.to_numpy(), y_df.to_numpy(), test_size=0.2, random_state=1)
    chi2_result = chi2_analysis(x_train_label_encoded, x_df, y_train)

    # to pick the selected best questions as features
    # Eg: choose the best 13 features as below
    df = pd.read_csv("WID3006 ML Questionnaire.csv")
    df = data_cleaning(df)
    df = data_encoding(df)
    df_norm = data_normalization(df)
    best_k_features = select_best_k_features(chi2_result, k=13)
    x = filter_features(best_k_features, df_norm)