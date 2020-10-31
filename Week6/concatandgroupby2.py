import pandas as pd
import numpy as np

from Week6.ggikko_helper import get_file_abs_path

df = pd.read_csv(get_file_abs_path('concat_salary.csv'))

print(df.head(10))

df['사업장명'] = df['사업장명'].str.strip()
df['사업장명'].replace('', np.nan, inplace=True)
df = df[df['사업장명'].notna()]
df.to_csv('concat_salary2.csv', index=False)