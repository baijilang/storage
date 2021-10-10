'''
需要键盘输入长度，需要键盘输入单位
'''
print("支持英寸和厘米的转换\n长度或单位输入exit可退出")
while True:
    lenth=input("请输入长度:")
    lenth1=lenth.replace(".","1")
    lenth2=lenth[0]
    unit=input("请输入原单位（inch/cm）：")
    if ((lenth.count(".")==1 and (lenth2!=".") )or (lenth.isdigit()))and(unit=="inch"or unit=="cm"):
        if unit=="inch":
            lenth=float(lenth)
            lentht=2.54*lenth
            print("%.2fcm"%(lentht))
        elif unit =="cm":
            lenth=float(lenth)
            lentht=lenth/2.54
            print("%.2finch"%(lentht))
    elif lenth=="exit" or unit=="exit":
        break
    else:
        print("请输入正确格式的长度或单位")
