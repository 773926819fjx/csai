import csv
from pandas.io.excel import ExcelWriter
import pandas as pd

wlist = [['月份', '营业额'], ['一月', 5555], ['二月', 6666], ['三月', 7777], ['四月', 4545],
         ['五月', 2565], ['六月', 5656], ['七月', 8321], ['八月', 4545], ['九月', 2165],
         ['十月', 3656], ['十一月', 7575], ['十二月', 1526]]

with open('营业额.csv', 'w', newline='', encoding='utf-8') as cfile:
    fwrite = csv.writer(cfile)
    fwrite.writerows(wlist)

with ExcelWriter('营业额.xlsx') as ew:  # pylint: disable=abstract-class-instantiated
    # 将csv文件转换为excel文件
    pd.read_csv("营业额.csv").to_excel(ew, sheet_name="Sheet1", index=False) 
