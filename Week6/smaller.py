import re

import pandas as pd
import os

from Week6.ggikko_helper import *

# http://www.albamon.com/list/gi/mon_area.asp

columns = ['자료생성년월', '사업장명', '사업자번호', '가입상태', '우편번호', '지번주소', '도로명주소', '법정주소코드',
           '행정주소코드', '광역시코드', '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명',
           '적용일', '재등록일', '탈퇴일', '가입자수', '고지금액', '신규', '상실', ]

pattern_1 = '\(.*\)'
pattern_2 = '\（.*\）'
pattern_3 = '주식회사'


# 광역시군구코드	코드명	코드명2자리	영문명
# 11	서울특별시	서울	Seoul
# 26	부산광역시	부산	Busan
# 27	대구광역시	대구	Daegu
# 28	인천광역시	인천	Incheon
# 29	광주광역시	광주	Gwangju
# 30	대전광역시	대전	Daejeon
# 31	울산광역시	울산	Ulsan
# 36	세종특별자치시	세종	Sejong
# 41	경기도	경기	Gyeonggi
# 42	강원도	강원	Gangwon
# 43	충청북도	충북	Chungcheongbuk
# 44	충청남도	충남	Chungcheongnam
# 45	전라북도	전북	Jeollabuk
# 46	전라남도	전남	Jeollanam
# 47	경상북도	경북	Gyeongsangbuk
# 48	경상남도	경남	Gyeongsangnam
# 50	제주특별자치도	제주	Jeju


def change_local_name_to_value(addr):
    return str(addr)[:2]


def text_preprocess(text):
    text = re.sub(pattern_1, '', text)
    text = re.sub(pattern_2, '', text)
    text = re.sub(pattern_3, '', text)
    return str(text).strip()


temp_df = pd.read_csv(get_file_abs_path("eight.csv")).copy()
temp_df.columns = columns
temp_df['인당고지금액'] = temp_df['고지금액'] / temp_df['가입자수']
temp_df['평균월급'] = temp_df['인당고지금액'] / 9 * 100
temp_df['평균연봉'] = int(temp_df['평균월급'].values[0] * 12)

# 사업장명 변경
temp_df['사업장명'] = temp_df['사업장명'].apply(text_preprocess)

# 가입상태만 보도록 수정
temp_df = temp_df.loc[temp_df['가입상태'] == 1]

print(temp_df.info())
print(temp_df.head(10))
temp_df["joinlossratio"] = round(temp_df["상실"] / temp_df["가입자수"] * 100, 2)

# 불필요 피쳐 제거
temp_df = temp_df.drop(
    ['자료생성년월', '우편번호', '법정주소코드', '사업자번호', '고지금액', '인당고지금액', '평균월급', '가입상태', '지번주소', '도로명주소', '행정주소코드', '상실', '가입자수',
     '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명', '적용일', '재등록일', '탈퇴일', '신규'],
    axis=1)

# print(temp_df['업종코드'].value_counts())
temp_df.to_csv(get_file_abs_path('eight.csv').replace("eight.csv", 'temp_eight.csv'), index=False)

#
# # 사업장명 간소화
# temp_df['사업장명'] = temp_df['사업장명'].apply(text_preprocess)
#
# # NonNull
# condition = temp_df['가입자수'].notnull() & temp_df['사업장명'].notnull()
# temp_df = temp_df.loc[condition, ["사업장명", "가입자수", "도로명주소", "신규", "상실", "고지금액", "평균연봉"]]
# temp_df = temp_df[temp_df['사업장명'].notnull()]
# # temp_df = temp_df.sort_values(by="평균연봉", ascending=False) => 동작안함
#
# print(path)
# temp_df.to_csv(path.replace("data", "refined"), index=False)  # 4000 row?
