'''
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
'''
print("输入分数(0-100)判断等级\n输入q退出")
while 2==2:
    grade=input("输入成绩:")
    m1=grade[0]
    m2=grade.count(".")
    m3=grade.replace(".","1")
    if grade.isdigit() or((m1!=".") and (m2==1) and (m3.isdigit())):
        grade=float(grade)
        if grade>=90 and grade<=100:
            print("A")
        elif grade>=80 and grade<90:
            print("B")
        elif grade>=70 and grade<80:
            print("C")
        elif grade>=60 and grade<70:
            print("D")
        elif grade>=0 and grade<60:
            print("E")
        else:
            print("输入数字不在范围")
    elif grade=="q":
        break
    else :
        print("输入非法")