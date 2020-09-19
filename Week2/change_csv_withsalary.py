import re
import pandas as pd

# change columns
columns = ['자료생성년월', '사업장명', '사업자번호', '가입상태', '우편번호', '지번주소', '도로명주소', '법정주소코드',
           '행정주소코드', '광역시코드', '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명',
           '적용일', '재등록일', '탈퇴일', '가입자수', '고지금액', '신규', '상실', ]

pattern_1 = '\(.*\)'
pattern_2 = '\（.*\）'
pattern_3 = '주식회사'


def text_preprocess(text):
    text = re.sub(pattern_1, '', text)
    text = re.sub(pattern_2, '', text)
    text = re.sub(pattern_3, '', text)
    return str(text)


# load data
for i in range(1, 2):
    print(str(i))
    path = "/Users/jihongpark/Documents/Week2/data/salary_0" + str(i) + "month.csv"
    temp_df = pd.read_csv(path).copy()
    print(temp_df.info())
    temp_df.columns = columns
    temp_df['인당고지금액'] = temp_df['고지금액'] / temp_df['가입자수']
    temp_df['평균월급'] = temp_df['인당고지금액'] / 9 * 100
    temp_df['평균연봉'] = int(temp_df['평균월급'].values[0] * 12)

    # 사업장명 간소화
    temp_df['사업장명'] = temp_df['사업장명'].apply(text_preprocess)

    # NonNull
    condition = temp_df['가입자수'].notnull() & temp_df['사업장명'].notnull()
    temp_df = temp_df.loc[condition, ["사업장명", "가입자수", "도로명주소", "신규", "상실", "고지금액", "평균연봉"]]
    temp_df = temp_df[temp_df['사업장명'].notnull()]
    # temp_df = temp_df.sort_values(by="평균연봉", ascending=False) => 동작안함

    print(path)
    temp_df.to_csv(path.replace("data", "refined"), index=False)  # 4000 row?
