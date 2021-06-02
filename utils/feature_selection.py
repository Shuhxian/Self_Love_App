import sys 
sys.path.append("../")
sys.path.append("../preprocessing")
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2, SelectKBest, RFECV
from sklearn.model_selection import train_test_split
from data_cleaning import *
from Data_Normalization import *
from sklearn.linear_model import LogisticRegression

    
def sort_by_questions(data, x_columns, ascending = False):
    """
    group the questions & answer features by questions as 1 question is encoded into several feature columns 
    """
    question_answers_score = pd.DataFrame(data, index=x_columns).reset_index()
    question_answers_score["Question"] = question_answers_score["index"].apply(lambda column_name : column_name.split("_")[0])
    question_score = question_answers_score.groupby("Question").mean().sort_values(0, ascending=ascending)
    return question_score

def rfe_cv(x_train, y_train, x_columns, y_columns, model, cv=5, scoring="f1_micro"):
    """
    - pick a model to evaluate the feature importance
    - ranking is used as the feature importance so the lower the score, the better it is
    - refer to https://machinelearningmastery.com/rfe-feature-selection-in-python/
    """
    min_features_to_select=1
    rfecv_by_class = []

    for i in range(y_train.shape[1]):
        rfecv = RFECV(model, step=1, cv=cv, scoring=scoring)
        rfecv.fit(x_train, y_train[:,i])
        rfecv_by_class.append(rfecv.ranking_)
        print("\nHobby:", y_columns[i])
        print("Best number of features:", rfecv.n_features_)
        print("Score:", rfecv.grid_scores_[rfecv.n_features_-1])
        for i in range(len(x_columns)): 
            # if the selected feature is included in the best number of features
            # print the feature name
            if rfecv.support_[i]:
                print(i+1, x_columns[i])

    rfecv_by_class = np.array(rfecv_by_class)
    rfe_result = sort_by_questions(np.mean(rfecv_by_class, axis=0), x_columns, ascending=True) 
    return rfe_result 

def chi2_analysis(x_train_label_encoded, x_label_encoded_df, y_train):
    """
    Why chi2 is suitable? can refer the link below
    https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/
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

    # to do Recursive Feature Elimination(rfe) feature selection
    df = pd.read_csv("WID3006 ML Questionnaire.csv")
    df = data_cleaning(df)
    df = data_encoding(df)
    df_norm = data_normalization(df)
    x = df_norm.iloc[:, :64]
    y = df_norm.iloc[:, 64:]
    x_numpy, y_numpy = x.to_numpy(), y.to_numpy()
    x_train, x_test, y_train, y_test = train_test_split(x_numpy, y_numpy, test_size=0.2, random_state=1)
    rfe_result = rfe_cv(x_train, y_train, x.columns, y.columns, LogisticRegression())

    # to pick the selected best questions as features
    # Eg: choose the best 13 features as below
    df = pd.read_csv("WID3006 ML Questionnaire.csv")
    df = data_cleaning(df)
    df = data_encoding(df)
    df_norm = data_normalization(df)
    # choose either chi2 or rfe 
    best_k_features = select_best_k_features(chi2_result, k=13) # choose chi2_result 
    best_k_features = select_best_k_features(rfe_result, k=13) # choose rfe_analysis
    x = filter_features(best_k_features, df_norm)

   