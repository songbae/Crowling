#크롤링해서 엑셀 파일로 만들기

# import openpyxl
# excel_file =openpyxl.Workbook()
# excel_sheet = excel_file.active
# excel_sheet.append(['data1','data2','data3'])
# excel_file.save('make_excel.xlsx')
# excel_file.close()
import requests
from bs4 import BeautifulSoup

res= requests.get('https://www.acmicpc.net/group/workbook/view/8918/29115')
soup= BeautifulSoup(res.content,'html.parser')
data= soup.select('#table_body')
for i in data:
    print(data)
