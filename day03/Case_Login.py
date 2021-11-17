# 从表格中导入用例
import xlrd
from xlutils import copy


def get_case(filepath, sheet_name):
    Login_Success_Case = []
    Login_Default_Case = []
    workbook = xlrd.open_workbook(filename=filepath, encoding_override=False)
    worksheet = workbook.sheet_by_name(sheet_name)
    rows = worksheet.nrows
    for i in range(1, rows):
        info = worksheet.row_values(i)
        if info[2] == 'Student Login':
            Login_Success_Case.append(info[:3])
        else:
            Login_Default_Case.append(info[:3])
    return Login_Success_Case, Login_Default_Case


def open_excel(filepath, sheet_name):
    f = xlrd.open_workbook(filename=filepath, encoding_override=False)
    r_sheet = f.sheet_by_name(sheet_name)
    index = 0
    for num, title in enumerate(r_sheet.row_values(0)):
        if title == '是否通过':
            index = num
            break
    new_workbook = copy.copy(f)
    new_sheet = new_workbook.get_sheet(sheet_name)
    return new_workbook, new_sheet, index


Login_Success_Case, Login_Default_Case = get_case('HkrTestCase.xlsx', 'Login')
print(Login_Success_Case, '\n', Login_Default_Case)
