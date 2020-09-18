import pandas as pd


def change_cp949_to_utf8(path: str):
    pd.read_csv(path, encoding="cp949").to_csv(path.replace("origin_", ""), index=False)


for i in range(1, 9):
    print(i)
    path = "/Users/jihongpark/Documents/Week2/data/salary_origin_0" + str(i) + "month.csv"
    change_cp949_to_utf8(path)
