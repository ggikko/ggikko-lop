# def change_local_name_to_value(addr: str):
#     # print(type(addr))
#     # print(addr)
#     if '서울특별시' in addr:
#         return 0
#     if '부산광역시' in addr:
#         return 1
#     else:
#         return 2


# print(change_local_name_to_value("서울특별시 핼로우"))
import pandas as pd
from datetime import datetime
from pandas import DataFrame

from Week6.ggikko_helper import get_file_abs_path

mm1 = pd.read_csv(get_file_abs_path('202001_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm2 = pd.read_csv(get_file_abs_path('202002_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm3 = pd.read_csv(get_file_abs_path('202003_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm4 = pd.read_csv(get_file_abs_path('202004_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm5 = pd.read_csv(get_file_abs_path('202005_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm6 = pd.read_csv(get_file_abs_path('202006_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm7 = pd.read_csv(get_file_abs_path('202007_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]
mm8 = pd.read_csv(get_file_abs_path('202008_refined.csv')).drop_duplicates(['사업장명'], keep='first').dropna(axis=0).loc[:,['사업장명', 'joinlossratio']]

root_df = mm8.copy()[120000:140000]

# print(mm1.shape)
# print(mm2.shape)
# print(mm3.shape)
# print(mm4.shape)
# print(mm5.shape)
# print(mm6.shape)
# print(mm7.shape)
# print(mm8.shape)

# (482274, 4)
# (477371, 4)
# (482167, 4)
# (483001, 4)
# (485742, 4)
# (486043, 4)
# (488228, 4)
# (489561, 4)

# (403910, 4)
# (399986, 4)
# (403928, 4)
# (404837, 4)
# (407105, 4)
# (407397, 4)
# (409120, 4)
# (410329, 4)

# mm3 = pd.read_csv(get_file_abs_path('202003_refined.csv'))

# mm2 = mm2.loc[:, ['사업장명', 'joinlossratio']]
# mm3 = mm3.loc[:, ['사업장명', 'joinlossratio']]


print("load complete")


def getCount(df, company_name: str):
    row = df[df['사업장명'] == company_name]['joinlossratio']
    if len(row) > 0:
        return row.values[0]
    else:
        return 0


new_joinlossratio_list = []

start = datetime.now()

for company in root_df['사업장명'].values:
    total_joinlossratio = 0
    total_joinlossratio += getCount(mm1, company)
    total_joinlossratio += getCount(mm2, company)
    total_joinlossratio += getCount(mm3, company)
    total_joinlossratio += getCount(mm4, company)
    total_joinlossratio += getCount(mm5, company)
    total_joinlossratio += getCount(mm6, company)
    total_joinlossratio += getCount(mm7, company)
    total_joinlossratio += getCount(mm8, company)
    total_joinlossratio = total_joinlossratio / 8
    new_joinlossratio_list.append(total_joinlossratio)
    # print(total_joinlossratio)
    print(company)

end = datetime.now()

print((end-start))

root_df['joinlossratio2'] = new_joinlossratio_list

root_df.to_csv("real_test9.csv", index=False)
print("complete")
# print(new_joinlossratio_list)

# print(mm1.shape)
# print(mm2.shape)
# print(mm3.shape)

# CHUNK_SIZE = 10000
# csv_file_list = [get_file_abs_path('202001_refined.csv'), get_file_abs_path('202002_refined.csv')]
#
# first_one = True
# for csv_file_name in csv_file_list:
#     if not first_one:  # if it is not the first csv file then skip the header row (row 0) of that file
#         skip_row = [0]
#     else:
#         skip_row = []
#
#     chunk_container = pd.read_csv(csv_file_name, chunksize=CHUNK_SIZE, skiprows=skip_row)
#     for chunk in chunk_container:
#         chunk.to_csv(output_file, mode="a", index=False)
#     first_one = False

# merge: DataFrame = pd.merge(mm1, mm2, on="사업장명", how='outer')
# merge = pd.concat([mm1, mm2]).drop_duplicates()
# merge = pd.merge(merge, mm3, on="사업장명", how='outer')
# merge.to_csv("merge.csv", index=False)
# merge = merge.dropna()
# print(merge.info())
# print(merge.shape)
# print(merge.head(100))
