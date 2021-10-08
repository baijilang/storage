# 10-90这个范围里面
# 如果猜大了打印”猜大了“ 猜小了
# 最多猜3次 锁屏 time.sleep(10)

import  random
import time
randint=random.randint(10,90)
print(randint)
print("一共3次机会")
num1=randint
count=int(3)
while True:
    num=int(input("猜猜随机数是多少"))
    count=count-1
    if num == num1 :
        print("真有你的")
        break
    else:
        if count==0 :
            print("失败,5秒后锁屏")
            time.sleep(1)
            print("4秒")
            time.sleep(1)
            print("3秒")
            time.sleep(1)
            print("2秒")
            time.sleep(1)
            print("1秒")
            time.sleep(1)
            from ctypes import *
            user32 = windll.LoadLibrary('user32.dll')
            user32.LockWorkStation()
            break
        else:
            if num > num1 and num <= 90 :
                print("%s,还有%d次机会"%('猜大了',count))
            else:
                print("%s,还有%d次机会"%('猜小了',count))
                continue






