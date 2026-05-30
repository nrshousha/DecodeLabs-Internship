import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os

def load_and_preprocess():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '..', 'data','mushrooms.csv')
    df = pd.read_csv(file_path)

    df_encoded = df.apply(LabelEncoder().fit_transform)

    X = df_encoded.drop(['class'], axis=1)
    Y = df_encoded['class']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size=0.2, random_state=42)

    return X_train, X_test, Y_train, Y_test