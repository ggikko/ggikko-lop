import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("/Users/jihongpark/Documents/Week2/Week3/data/fc-ml-titanic.csv")

feature = [
    'Pclass',
    'Sex',
    'Age',
    'Fare',
]

label = ['Survived']

x_train, x_valid, y_train, y_valid = train_test_split(train[feature], train[label], test_size=0.2, shuffle=True,
                                                      random_state=30)
# print(x_train.shape)
# print(y_train.shape)
# print(x_valid.shape)
# print(y_valid.shape)
#
# print(train.isnull().sum())

# imputer = SimpleImputer(strategy="mean")
# imputer.fit(train[['Pclass', 'Age']])
# result = imputer.transform(train[['Pclass', 'Age']])
# print(result)

# train[['Pclass', 'Age']] = result


# print(train[['Pclass', 'Age']])
# print(train['Pclass', 'Age'])

# print(train.isnull().sum())

# print(train['Sex'].value_counts())

encoder = LabelEncoder()

train['Sex_num'] = encoder.fit_transform(train['Sex'])
print(train['Sex_num'].value_counts())
print(encoder.classes_)

train['Sex_num'] = encoder.inverse_transform(train['Sex_num'])
print(train['Sex_num'].value_counts())

print(train['Sex_num'][:])
# print(transform)

# 지식 맛보기
# Sklearn 익숙해지기
# 결측치
# 이상치 null처리, one hot encoding
# 정규화 scale normalization
# 표준화
# 샘플링
# 피처공학
# 피처 생성/연산
# 구간생성, 스케일 변형
