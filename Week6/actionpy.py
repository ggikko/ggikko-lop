import re

import pandas as pd
from pandas import DataFrame

from Week6.ggikko_helper import refined_salary_data, get_file_abs_path, change_column


def getRatioCount(df: DataFrame, company_name: str):
    find = df.loc[df['joinlossratio'].str.contains(company_name, regex=False)].head(1)
    if hasItem(find):
        return find["joinlossratio"].values[0]
    else:
        return 0


def hasItem(df):
    if len(df) > 0:
        return True
    else:
        return False


# refined_salary_data("202001.csv")
# refined_salary_data("202002.csv")
# refined_salary_data("202003.csv")
# refined_salary_data("202004.csv")
# refined_salary_data("202005.csv")
# refined_salary_data("202006.csv")
# refined_salary_data("202007.csv")
# refined_salary_data("202008.csv")

temp_list: list = []

# temp_list.append(pd.read_csv(get_file_abs_path('202001.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202002.csv')))

temp_list.append(pd.read_csv(get_file_abs_path('202001_refined.csv')))
temp_list.append(pd.read_csv(get_file_abs_path('202002_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202003_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202004_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202005_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202006_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202007_refined.csv')))
# temp_list.append(pd.read_csv(get_file_abs_path('202008_refined.csv')))

# temp_list[0]['joinlossratio'] = temp_list[0]['joinlossratio'].add(temp_list[1]['joinlossratio'], fill_value=0)
# print(temp_list[0]['joinlossratio'])

root_df: DataFrame = temp_list[0]
second_df: DataFrame = temp_list[1]

# def hoho(company_name):
#     find = temp_list[0].loc[temp_list[0]['사업장명'] == company_name].head(1)
#     if hasItem(find):
#         return find["joinlossratio"]
#     else:
#         return temp_list[0]

# def root(root_df: DataFrame):
#     return root_df[root_df['사업장명'].isin(temp_list[1]['사업장명'])]
#     pass
# m = root_df.merge(second_df, on='사업장명', how='inner', suffixes=['', '_'], indicator=True)

df = root_df.merge(second_df, on=['사업장명'], how='left')

print(df.info())
print(df.shape)
print(df.head(10))


# root_df.apply()

# print(second_df.head(100))

# root_df['joinlossratio2'] = temp_list[1][temp_list[1]['사업장명'].isin(root_df['사업장명'])]['joinlossratio']
# print(test.info())
# print(test.head(100))
# print(test.head(100))

# root_df.to_csv("tttt", index=False)


# temp_list[1]['사업장명'].apply(hoho)

# print(temp_list[1].info())


# 사업자번호
# first = change_column(temp_list[0])
# second = change_column(temp_list[1])

# test = first.loc[:, first['사업장명'] == second['사업장명']]
# print(test.info())

# root_df: DataFrame = temp_list[7]

# temp_df = root_df.copy()

# temp_list[0]['사업장명'] = temp_list[0]['사업장명'].astype(str)
# temp_list[1]['사업장명'] = temp_list[1]['사업장명'].astype(str)


# temp_list[0]['사업장명'] = temp_list[0]['사업장명'].str.encode('utf-8')
# temp_list[1]['사업장명'] = temp_list[1]['사업장명'].str.encode('utf-8')

# temp_list[0]['사업장명'] = temp_list[0]['사업장명'].apply(lambda x: re.findall(x, x))
# temp_list[1]['사업장명'] = temp_list[1]['사업장명'].apply(lambda x: re.findall(x, x))

# root하나 지정 -> 하나씩 찾아서 더하기


# temp_list[1]["가입자수2"] = temp_list[1]["가입자수"]
# temp_list[1] = temp_list[1].loc[:, ['사업장명', '가입자수2']]
# merge: DataFrame = pd.merge(temp_list[0], temp_list[1], on="사업장명", how='outer')
# # merge = temp_list[0].merge(temp_list[1], how='left', on=['사업자번호'])
# print(merge.head(100))
# print(merge.shape)
# # temp_list[0]['test'] = merge['가입자수'].values
#
# print(temp_list[0].shape)
# print(temp_list[1].shape)


# print(merge.info())
# print(merge.shape)
# print(merge.head(50))


# merge: DataFrame = pd.concat([temp_list[0], temp_list[1]], axis=1)

# temp_list[0].head(10).to_csv("mergetest1.csv", index=False)
# temp_list[1].head(10).to_csv("mergetest2.csv", index=False)

# merge.to_csv("test22", index=False)
# merge: DataFrame = temp_list[0].merge(temp_list[1], on="사업장명")
# print(merge.info())


# for temp_df in temp_list:
#     join_total_count += getRatioCount(temp_df, target_company)
#     leave_total_count += getLeaveCount(temp_df, target_company)
#     month_salary_total_count += getSalary(temp_df, target_company)
#     pass


def applyJoinlossratio(df: DataFrame):
    count = getRatioCount(df, df['사업장명'])
    print(count)
    return count

    # df['joinlossratio']
    # for ddd in temp_list:
    #     getRatioCount(ddd)

# temp_df.apply(applyJoinlossratio)
#
# temp_df['joinlossratio'] = temp_df.apply(applyJoinlossratio)
