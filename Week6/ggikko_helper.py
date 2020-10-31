import os
import re

import pandas as pd
from pandas import DataFrame


def get_file_abs_path(file_name: str):
    absolute_path = os.path.abspath(os.path.dirname(file_name))
    file_path = absolute_path + "/data/" + file_name
    return file_path


pattern_1 = '\(.*\)'
pattern_2 = '\（.*\）'
pattern_3 = '주식회사'


def text_preprocess(text):
    text = re.sub(pattern_1, '', text)
    text = re.sub(pattern_2, '', text)
    text = re.sub(pattern_3, '', text)
    return str(text).strip()


def change_column(df) -> DataFrame:
    columns = ['자료생성년월', '사업장명', '사업자번호', '가입상태', '우편번호', '지번주소', '도로명주소', '법정주소코드',
               '행정주소코드', '광역시코드', '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명',
               '적용일', '재등록일', '탈퇴일', '가입자수', '고지금액', '신규', '상실', ]
    df.columns = columns
    return df


def smaller(origin_df: DataFrame) -> DataFrame:
    temp_df = origin_df.copy()

    change_column(temp_df)

    temp_df['평균연봉'] = ((temp_df['고지금액'] / temp_df['가입자수']) / 9 * 100) * 12
    temp_df = temp_df[temp_df['평균연봉'].notna()]
    temp_df['사업장명'] = temp_df['사업장명'].apply(text_preprocess)

    # 가입상태만 보도록 수정
    temp_df = temp_df.loc[temp_df['가입상태'] == 1]

    temp_df["joinlossratio"] = round(temp_df["상실"] / temp_df["가입자수"] * 100, 5)

    # 불필요 피쳐 제거
    temp_df = temp_df.drop(
        ['자료생성년월', '우편번호', '법정주소코드', '사업자번호', '고지금액', '가입상태', '지번주소', '도로명주소', '행정주소코드', '상실', '가입자수',
         '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명', '적용일', '재등록일', '탈퇴일', '신규'],
        axis=1)
    return temp_df


def refined_salary_data(file_name: str, need_save: bool = False) -> DataFrame:
    if need_save:
        df = smaller(pd.read_csv(get_file_abs_path(file_name)))
        df.to_csv(
            get_file_abs_path(file_name).replace(".csv", "_refined.csv"), index=False)
    else:
        df = smaller(pd.read_csv(get_file_abs_path(file_name)))
    return df
