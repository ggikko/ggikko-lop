import pandas as pd

from Week6.ggikko_helper import get_file_abs_path

mm1 = pd.read_csv(get_file_abs_path('202001_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm2 = pd.read_csv(get_file_abs_path('202002_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm3 = pd.read_csv(get_file_abs_path('202003_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm4 = pd.read_csv(get_file_abs_path('202004_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm5 = pd.read_csv(get_file_abs_path('202005_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm6 = pd.read_csv(get_file_abs_path('202006_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm7 = pd.read_csv(get_file_abs_path('202007_refined.csv')).drop_duplicates(['사업장명'], keep='first')
mm8 = pd.read_csv(get_file_abs_path('202008_refined.csv')).drop_duplicates(['사업장명'], keep='first')

print(mm8.shape)

concat_df = pd.concat([mm1, mm2, mm3, mm4, mm5, mm6, mm7, mm8], axis=0)
concat_df = concat_df[concat_df['사업장명'].notna()]
groupby_df = concat_df.groupby(['사업장명'])

new_df = pd.DataFrame(
    {'사업장명': groupby_df['사업장명'].first(), '광역시코드': groupby_df['광역시코드'].first(), '평균연봉': groupby_df['평균연봉'].mean(),
     'joinlossratio': groupby_df['joinlossratio'].mean()})

# 사업장명,광역시코드,평균연봉,joinlossratio

# print(concat.shape)
# print(concat.head(10))


# mean = groupby['joinlossratio']

new_df = new_df.reset_index(drop=True)
new_df.to_csv("concat_salary.csv", index=False)

# print(groupby.count())
print(new_df.head(30))
print(type(new_df))
