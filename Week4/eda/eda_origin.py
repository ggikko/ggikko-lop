import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv('data/salary_08month.csv')

train["가입대비상실"] = round(train["상실"] / train["가입자수"] * 100, 2)
train["평균월급"] = train["평균월급"].astype(int)
train["사업장명"] = train["사업장명"].str.strip()

# train = train.loc[train['가입자수'] > 500, :]
# upper_100_join = train.loc[train['신규'] > train['상실'], :]
values = train.sort_values(by='가입대비상실', ascending=False)

# 추출하고 원하지 않은 이상한 값들은 손수 제거함

# print(train.head())
# print(train.corr())
# plt.figure(figsize=(12, 12))
# sns.heatmap(data=abs(train.corr()), annot=True, fmt='.2f', linewidths=.5, cmap='coolwarm')
# plt.show()

print(train.info())
print(train.describe())

# plt.figure(figsize=(9, 9))
# plt.subplot(3, 3, 1)
# sns.distplot(train.iloc[:, 1])
# plt.subplot(3, 3, 2)
# sns.distplot(train.iloc[:, 3])
# plt.subplot(3, 3, 3)
# sns.distplot(train.iloc[:, 4])
# plt.subplot(3, 3, 4)
# sns.distplot(train.iloc[:, 5])
# plt.subplot(3, 3, 5)
# sns.distplot(train.iloc[:, 6])
# plt.subplot(3, 3, 6)
# sns.distplot(train.iloc[:, 7])
# plt.subplot(3, 3, 7)
# sns.distplot(train.iloc[:, 8])
# plt.tight_layout()
# plt.show()
