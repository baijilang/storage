'''
输入年份判断是否是闰年
闰年：能被4整除
'''
print("输入e退出")
while True:
    year = input("请输入年份：")
    if year.isdigit() :
        year=int(year)
        if year/4==int(year/4):
            print("%d是闰年"%(year))
        else:
            print(("%d不是闰年"%(year)))
    elif year =="e":
        break
    else :
        print("请输入整数数字")