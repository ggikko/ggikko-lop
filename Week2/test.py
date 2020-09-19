import time
import math
import pandas as pd

# print(format(1234, ","))
# time.sleep(2)
# time.sleep(1)
# startTime = time.time()
# endTime = time.time()
# start_time = endTime - startTime
# print(int(start_time))

path = "/Users/jihongpark/Documents/Week2/refined/salary_01month.csv"
csv = pd.read_csv(path)
isnull = pd.isnull(csv["사업장명"])
isnull_ = csv[isnull]
# fillna = csv.fillna(0)
# isnull_ = csv.loc[csv.isna(), :]
print(isnull_)
