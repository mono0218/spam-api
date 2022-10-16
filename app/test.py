import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import pickle

# CSV読み込み
df = pd.read_csv('spam.csv', encoding='latin-1')
# 未使用列を削除
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
# リネーム
df.rename(columns={"v1": "class", "v2": "text"}, inplace=True)

df.head()

X = pd.DataFrame(df['text'])
Y = pd.DataFrame(df['class'])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=10)

vec_count = CountVectorizer(min_df=3)
vec_count.fit(X_train['text'])

# トレーニング・評価データをベクトル化
X_train_vec = vec_count.transform(X_train['text'])
X_text_vec = vec_count.transform(X_test['text'])

model = BernoulliNB()
model.fit(X_train_vec, Y_train['class'])
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


def mono(req):
    data = np.array([req])
    df_data = pd.DataFrame(data, columns=['text'])
    input_vec = vec_count.transform(df_data['text'])
    model.predict(input_vec)
    return model.predict(input_vec)
