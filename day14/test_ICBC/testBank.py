from unittest import TestCase
import unittest
from ddt import data
from ddt import ddt
from ddt import unpack
from BankTool import Bank
import xlrd
from xlutils import copy

# 生成数据
da1 = [['123456', 'zhangsna', '2', '123456', '中国', '北京', '华盛街', 's001', 1],
       ['123456', 'zhangsn', '1', '123456', '中国', '北京', '华盛街', 's001', 1],
       ['123456', 'zhangs', '1', '123456', '中国', '北京', '华盛街', 's001', 1],
       ['123456', 'zhang', '1', '12356', '中国', '北京', '华盛街', 's001', 5]]  # 添加用户测试

def get_data(data_path,data_sheet_name):
    data_workbooks = xlrd.open_workbook(data_path, formatting_info=True)
    data_sheet = data_workbooks.sheet_by_name(data_sheet_name)
    data_rows = data_sheet.nrows
    new_data = [data_sheet.row_values(i)[0:3] for i in range(1, data_rows) if data_sheet.row_values(i)[0] != '']
    new_workbook = copy.copy(data_workbooks)
    new_sheet = new_workbook.get_sheet(data_sheet_name)
    return [new_data, new_sheet, data_sheet, new_workbook,data_workbooks]  # 【复制后的数据、复制的表单、复制前表单，复制后的工作簿，复制前的工作簿】
def save_file(new_workbook, save_path):
    new_workbook.save(save_path)

# #####
path = r'bank_data.xls'
sheet_name = 'savemoney'
path_new = r'test_result.xls'
DATA2 = get_data(path, sheet_name)            # [da2, w_sheet, r_sheet, w_workbook,data_workbook]
data2 = DATA2[0]
w_sheet2 = DATA2[1]
w_worksheet2 = DATA2[3]
r_sheet = DATA2[2]
test2_result_list = []  # 记录测试结果存款测试

DATA3 = [[DATA2[4].sheet_by_name('转账测试').row_values(i)[0:5] for i in range(1, DATA2[4].sheet_by_name('转账测试').nrows) if DATA2[4].sheet_by_name('转账测试').row_values(i)[0] != ''],
         DATA2[3].get_sheet('转账测试'),DATA2[4].sheet_by_name('转账测试'),DATA2[3],DATA2[4]]
data3 = DATA3[0]
w_sheet3 = DATA3[1]
w_worksheet3 = DATA3[3]
# r_sheet = DATA3[2]
test3_result_list = []

# ####


bank = Bank()

@ddt
class TestaddUser(TestCase):

    @data(*da1)
    @unpack
    def test_adduser(self, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        result = bank.addUser(a1, a2, a3, a4, a5, a6, a7, a8)
        self.assertEqual(result, a9)

    @data(*data2)
    @unpack
    def test_savemoney(self, account, money, i):
        global path_new, w_sheet2, w_workbook, test2_result_list
        result2 = bank.savemoney(account, money)
        if result2 == int(i) :
            test2_result_list.append('pass')
            # print(result2,i)
        else:
            test2_result_list.append('fail')
        print(test2_result_list)
        if len(test2_result_list) ==len(data2):
            for index, value in enumerate(test2_result_list):
                w_sheet2.write(index + 1, 4, value)
        self.assertEqual(result2, i)


    @data(*data3)
    @unpack
    def test_transmoney(self, account_out, password_out,account_in, money, i):
        global DATA3,w_worksheet2,path_new
        result = bank.transmoney(account_out, password_out,account_in, money)
        # 1  2
        self.assertEqual(result, i)
        if  result == i:
            test3_result_list.append('pass')
        else:
            test3_result_list.append('fail')
        if len(test3_result_list) == len(data3):
            for index, value in enumerate(test3_result_list):
                w_sheet3.write(index + 1, 5, value)
            save_file(DATA3[3],path_new)
            print('success')



if __name__ == '__main__':

    unittest.main()
