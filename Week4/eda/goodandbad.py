import graphviz
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import seaborn as sns

#### 좋은기업 - 인터넷
##### 나쁜기업

# 실업자 순으로 위에서부터 아래로
# 패스 : 쿠팡, 맥도날드,
# 통과 :
# 이유 : 플래닛리뷰, 평점3점이하, 리뷰10개이상 , 연봉, 상실수, 뉴스 주관적으로 골라봄.. ;;

# 파생 컬럼을 추가함
# 가입대비상실 => 연봉과 관련이 있음 0.25  0.25면 관련 있다고 봐야하는가?
# 중견기업으로할까..? 가입자수가 낮으니 정보가 너무 없어서 나쁜 기업 판단하기 힘듬

# 좋은회사 : 검색

# 회사이름 trim 걸어야함

bad_corp_list = [
    "키스템프엠엔씨에스",
    "한국고용정보",
    "고양시청",
    "비케이알",
    "비지에프휴먼넷",
    "보보스링크",
    "에이스휴먼파워",
    "코리아세븐",
    "키스템프엘비에스",
    "동호에이치알",
    "더맨",
    "서빅",
    "사람인에이치에스",
    "무인양품",
    "유베이스",
    "유안에이치알",
    "윌앤비전",
    "트랜스코스모스코리아",
]

good_corp_list = [
    "케이비신용정보",
    "한국서부발전",
    "카카오엔터프라이즈",
    "구글코리아 유한회사",
    "카카오페이",
    "한국중부발전",
    "듀폰코리아",
    "한국남동발전",
    "한국지역난방공사",
    "한국남부발전",
    "네이버",
    "한국동서발전",
    "베인앤드컴퍼니코리아인크",
    "인천국제공항공사",
    "대학내일",
    "에스케이텔레콤",
    "바이켐",
    "한국수력원자력",
    "바이켐",
    "한국수력원자력",
    "에스케이증권",
    "아린엠에이치씨",
    "기아자동차",
    "브레이브모바일",
    "카카오",
    "한국얀센"
]


def filter_corp(data_frame, corp_list):
    temp = data_frame.loc[origin_df['사업장명'].isin(corp_list), :].copy()
    temp = temp.sort_values(by='가입대비상실', ascending=False)
    return temp


rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

origin_df = pd.read_csv('data/salary_08month.csv')

origin_df["가입대비상실"] = round(origin_df["상실"] / origin_df["가입자수"] * 100, 2)
origin_df["평균월급"] = origin_df["평균월급"].astype(int)
origin_df["사업장명"] = origin_df["사업장명"].str.strip()

# train = train.loc[train['가입자수'] > 500, :]
# upper_100_join = train.loc[train['신규'] > train['상실'], :]
origin_df = origin_df.sort_values(by='가입대비상실', ascending=False)

test_df = origin_df.loc[:100, :].copy()

# 좋은기업 추출
good_corp_df = filter_corp(origin_df, good_corp_list)
good_corp_df['status'] = 1
# print(good_corp_df.head(5))

# 나쁜기업 추출
bad_corp_df = filter_corp(origin_df, bad_corp_list)
bad_corp_df['status'] = 0
# print(bad_corp_df.head(5))

train_df = pd.concat([good_corp_df, bad_corp_df])

train_df.to_csv("train.csv", index=False)

# 추출하고 원하지 않은 이상한 값들은 손수 제거함

# print(train.head())
# print(train.corr())
# plt.figure(figsize=(12, 12))
# sns.heatmap(data=abs(train.corr()), annot=True, fmt='.2f', linewidths=.5, cmap='coolwarm')
# plt.show()

# print(origin_df.info())
#
# plt.figure(figsize=(12, 12))
# # for i in range(1, 13):
# plt.subplot(3, 4, 1)
# sns.distplot(train.iloc[:, 1])
# plt.subplot(3, 4, 3)
# sns.distplot(train.iloc[:, 3])
# plt.subplot(3, 4, 4)
# sns.distplot(train.iloc[:, 4])
# plt.subplot(3, 4, 5)
# sns.distplot(train.iloc[:, 5])
# plt.subplot(3, 4, 6)
# sns.distplot(train.iloc[:, 6])
# plt.subplot(3, 4, 7)
# sns.distplot(train.iloc[:, 7])
# plt.subplot(3, 4, 8)
# sns.distplot(train.iloc[:, 8])
# plt.subplot(3, 4, 9)
# sns.distplot(train.iloc[:, 9])
# plt.tight_layout()
# plt.show()

train_features = train_df.drop(['사업장명', '도로명주소'], axis=1)
train_labels = train_df['status']
test_features = test_df.loc[:100, :]
# print(test_df)

x_train, x_valid, y_train, y_valid = train_test_split(train_features, train_labels, stratify=train_labels,
                                                      random_state=42)

clf = DecisionTreeClassifier(max_depth=6, random_state=42)
clf.fit(x_train, y_train)
prediction = clf.predict(x_valid)

prediction_mean = (prediction == y_valid).mean()
print(prediction_mean)

# [0 0 1 0 1 1 1 1 0 1 0]
# [0 0 1 0 1 1 1 1 0 1 0]

# def show_trees(model2):
#     export_graphviz(model2, out_file="tree.dot",
#                     feature_names=x_train.columns,
#                     precision=3, filled=True)
#     with open("tree.dot") as f:
#         dot_graph = f.read()
#
#     g = graphviz.Source(dot_graph)
#     g.format = 'svg'
#     g.filename = 'tree2.dot'
#     g.directory = '/Users/jihongpark/Documents/example/ggikko-lop/Week4/eda/image/'
#
#     g.render(view=False)

# plt.figure(figsize=(40, 20))
# export_graphviz(clf, out_file="tree.dot",
#                 feature_names=x_train.columns,
#                 precision=3, filled=True)

# with open("/Users/jihongpark/Documents/example/ggikko-lop/Week4/eda/tree.png") as f:
#     dot_graph = f.read()
#
# dot = graphviz.Source(dot_graph)
# dot.format = "png"
# dot.render(filename='tree.png')

plt.figure(figsize=(12, 12))
sns.heatmap(data=abs(train_df.corr()), annot=True, fmt='.2f', linewidths=.5, cmap='coolwarm')
plt.show()
# brew install graphviz

# tree.plot_tree(clf)
# _ = tree.plot_tree(clf,
#                    out_file='tree.dot',
#                    feature_names=train_features,
#                    class_names=train_labels)
# plt.show()
# plt.savefig('filename.png')

# fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
# tree.plot_tree(clf,
#                feature_names=train_features,
#                class_names=train_labels,
#                filled=True);
# fig.savefig('imagename.png')

# show_trees(model)
# print(clf)
# 파생 컬럼 만들어서 지역 비교
# 평균 급여 애매쓰 파생을 만들어야
# heat map에서 얻을게 없다..
# 좋은 기업,나쁜 기업을 어느정도 분류해서 1과 0으로 만들어보고 다시 해볼까

# train test validation

# .dot 파일로 export 해줍니다

# 생성된 .dot 파일을 .png로 변환

# https://gist.github.com/WillKoehrsen/ff77f5f308362819805a3defd9495ffd
