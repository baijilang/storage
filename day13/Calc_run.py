from HTMLTestRunner import HTMLTestRunner
import unittest

# 加载所有用例
tests = unittest.defaultTestLoader.discover('.\\',pattern='test*.py')

# 创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = '计算器测试报告',
    description = '计算器的运算功能测试报告',
    verbosity = 1,
    stream=open(file='计算器的测试报告.html', mode='w+', encoding='utf8')
)

# 运行
runner.run(tests)



