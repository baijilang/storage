'''现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
[罗恩, 23 ,35 ,44]
[哈利 ,60, 77 ,68 ,88, 90]
[赫敏, 97 ,99 ,89 ,91, 95, 90]
[马尔福 ,100, 85 ,90]
求每个人的总成绩？'''
Ron=['罗恩', 23 ,35 ,44]
Harry=['哈利' ,60, 77 ,68 ,88, 90]
Homin=['赫敏', 97 ,99 ,89 ,91, 95, 90]
Marful=['马尔福' ,100, 85 ,90]
def Grade(x):
    T_grade=0
    for i in x:
        if type(i)!=str:
            T_grade+=float(i)
    return (T_grade)
print(Grade(Ron))
print(Grade(Harry))
print(Grade(Homin))
print(Grade(Marful))
