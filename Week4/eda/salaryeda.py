import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc

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


def hasContainsInList(name, corp_list):
    for corp in corp_list:
        if corp == name:
            return True
    return False


def save_filter_corp(data_frame, corp_list, path_name):
    temp = data_frame.loc[train['사업장명'].isin(corp_list), :]
    temp = temp.sort_values(by='가입대비상실', ascending=False)
    temp.to_csv(path_name)


rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv('data/salary_08month.csv')
print(train.info())

train["가입대비상실"] = round(train["상실"] / train["가입자수"] * 100, 2)
train["평균월급"] = train["평균월급"].astype(int)
train["사업장명"] = train["사업장명"].str.strip()

# train = train.loc[train['가입자수'] > 500, :]
# upper_100_join = train.loc[train['신규'] > train['상실'], :]
values = train.sort_values(by='가입대비상실', ascending=False)

# 좋은기업 추출
save_filter_corp(train, good_corp_list, '/Week4/eda/data/good_corp.csv')

# 나쁜기업 추출
save_filter_corp(train, bad_corp_list, '/Week4/eda/data/bad_corp.csv')

# 추출하고 원하지 않은 이상한 값들은 손수 제거함

# print(train.head())
# print(train.corr())
# plt.figure(figsize=(12, 12))
# sns.heatmap(data=abs(train.corr()), annot=True, fmt='.2f', linewidths=.5, cmap='coolwarm')
# plt.show()

# 파생 컬럼 만들어서 지역 비교
# 평균 급여 애매쓰 파생을 만들어야
# heat map에서 얻을게 없다..
# 좋은 기업,나쁜 기업을 어느정도 분류해서 1과 0으로 만들어보고 다시 해볼까
