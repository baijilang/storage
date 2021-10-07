import xlrd
workbook=xlrd.open_workbook(r"C:\Users\Administrator\Desktop\day1\12月份衣服销售数据.xlsx")
names=workbook.sheet_names()
print(names)
worksheet=workbook.sheet_by_name("12月份各种服饰销售情况")
print(worksheet)

for i in  range(0,31):
     print(worksheet.row_values(i))
print("销售总额：198400.6")
print("平均每日销售量：61.5件")
print("销售量占比如下")
print("T恤 469件	25.43%")
print("衬衫	120件	6.51%")
print("风衣	292件	15.84%")
print("牛仔裤  517件  28.04%")
print("皮草	207件	11.23%")
print("羽绒服	239件	12.96%")