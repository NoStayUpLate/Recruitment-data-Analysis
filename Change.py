import pandas as pd

data_xls = pd.read_excel("./ExcelFile/拉钩-汇总.xlsx",index_col=0)
data_xls.to_csv("./Lagou_All.csv",encoding='utf-8')

