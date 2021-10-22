import xlrd

# 拿到工作簿
wb = xlrd.open_workbook(filename=r'2020年每个月的销售情况.xlsx',encoding_override=True)

# 选择一个选项卡
st = wb.sheet_by_name("1月")

rows = st.nrows  # 获取有多少行
cols = st.ncols     # 获取有多少列


#  平均年龄，总工资
sal_sum = 0
age_sum = 0
for i in range(1,rows):
    data = st.row_values(i)
    sal_sum = sal_sum + data[1]
    age_sum = age_sum + data[2]

print("总工资为：",sal_sum,"，平均年龄为：",(age_sum / 3))