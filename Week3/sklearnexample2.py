from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()
# print(iris['DESCR'])
# print(type(iris))
# print(type(iris['data']))
# print(iris['target'])
# print(type[iris['target']])
names_ = iris['feature_names']
print(len(names_))
print(type(names_))
# print(names_.shpae)
# print(iris.describe())
# print(iris.info())

data_ = iris['data']
print(len(data_))
print(type(data_))
print(data_.shape)

df = pd.DataFrame(data_, columns=names_)
df['target'] = iris['target']

print(df.iloc[1:14, 15, 16])

print(df.info())
# print(df.loc[df['target'] == '1', :].values)

sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', data=df, palette='muted', hue='target')
plt.title("hello")
plt.show()

# print(df.describe())
# print(df.info())
