'''
从键盘输入任意三边，判断是否能形成三角形，
若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
###################################################
while True:
    a = input("请输入a:")
    b = input("请输入b:")
    c = input("请输入c:")
    if a.isdigit() and b.isdigit() and c.isdigit():
        a=int(a)
        b=int(b)
        c=int(c)
        tri=[a,b,c]
        tri.sort(reverse=False)
        if ((tri[0]+tri[1])>tri[2]) and (tri[0]>0):
            if tri[0]==tri[1] and tri[0]!=tri[2]:
                print("等腰三角形")
            if tri[0]==tri[1] and tri[0]==tri[2]:
                print("等边三角形")
            if (tri[0] * tri[0] + tri[1] * tri[1]) > (tri[2]*tri[2]):
                print("锐角三角形")
            if (tri[0] * tri[0] + tri[1] * tri[1]) == (tri[2]*tri[2]):
                print("直角三角形")
            if (tri[0] * tri[0] + tri[1] * tri[1]) < (tri[2]*tri[2]):
                print("钝角三角形")
            print(tri)
        else:
            print("无法组成三角形")
    elif a=="q" or b=="q" or c=="q":
        break
    else:
        print("不支持字符  ",end='')
