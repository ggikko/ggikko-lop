import pandas as pd
import numpy as np
from pycaret.classification import *
from sklearn.model_selection import train_test_split

from Week6.ggikko_helper import get_file_abs_path

# 사업장명,광역시코드,평균연봉,joinlossratio
sample = pd.read_csv(get_file_abs_path('train.csv'))

sample['joinlossratio'] = sample['가입대비상실']
print(sample.info())
print(sample.shape)
sample = sample.loc[:, ['사업장명', '광역시코드', '평균연봉', 'joinlossratio', 'status']]

sample.to_csv("train2.csv", index=False)

# 사업장명,광역시코드,평균연봉,joinlossratio

# 사업장명,가입자수,도로명주소,신규,상실,고지금액,평균월급,평균연봉,가입대비상실,status


# 베인앤드컴퍼니코리아인크,181,서울특별시 중구 퇴계로,10,14,74173220,4553297,54639572,7.73,1
# 브레이브모바일,61,경기도 성남시 분당구 황새울로200번길,6,4,17825180,3246845,38962142,6.56,1
# 카카오페이,544,경기도 성남시 분당구 판교역로,12,12,214293900,4376917,52523014,2.21,1


# train_features = sample['사업장명', '도로명주소']
# train_labels = train_df['status']
# test_features = test_df.loc[:100, :]
#
# x_train, x_valid, y_train, y_valid = train_test_split(sample[feature], sample[label], test_size=0.2, shuffle=True,
#                                                       random_state=30)
#
# print(df.head(10))
#
# df['사업장명'] = df['사업장명'].str.strip()
# df['사업장명'].replace('', np.nan, inplace=True)
# df = df[df['사업장명'].notna()]
# df.to_csv('concat_salary2.csv', index=False)
