import pandas as pd
from pycaret.classification import *
from sklearn.model_selection import train_test_split

from Week6.ggikko_helper import get_file_abs_path

# '사업장명', '광역시코드', '평균연봉', 'joinlossratio'
sample = pd.read_csv(get_file_abs_path('train2.csv'))
train = sample.drop(['사업장명'], axis=1)
features = sample.loc[:, ['광역시코드', '평균연봉', 'joinlossratio']]

train_features = features
train_labels = sample['status']

x_train, x_valid, y_train, y_valid = train_test_split(train_features, train_labels, stratify=train_labels,
                                                      random_state=42)

print(x_train.head(10))
print(x_train.shape)
print(y_train.head(10))
print(y_train.shape)
# sample.to_csv("train2.csv", index=False)

SEED = 14

clf = setup(data=train, target='status',
            session_id=SEED,
            categorical_imputation='mode',
            train_size=0.8,
            profile=True
            )

print(compare_models(sort='AUC', n_select=3))
