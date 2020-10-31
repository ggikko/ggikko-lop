import pandas as pd
import os


def change_cp949_to_utf8(file_name: str):
    path = '/Users/jihongpark/Documents/example/ggikko-lop/Week6/data/' + file_name
    pd.read_csv(path, encoding="cp949").to_csv(path, index=False)


change_cp949_to_utf8('202001.csv')
change_cp949_to_utf8('202002.csv')
change_cp949_to_utf8('202003.csv')
change_cp949_to_utf8('202004.csv')
change_cp949_to_utf8('202005.csv')
change_cp949_to_utf8('202006.csv')
change_cp949_to_utf8('202007.csv')
change_cp949_to_utf8('202008.csv')
