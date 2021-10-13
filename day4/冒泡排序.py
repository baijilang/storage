'''请对下列列表进行冒泡排序（网易测试开发笔试题）
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]'''
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
times_a=0
while True:
    count=0
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            m=a[i]
            a[i]=a[i+1]
            a[i+1]=m
            count+=1
            times_a+=1
    if count==0:
        print("一共调整了%d次"%(times_a))
        print("最终排序为:",a)
        break
    else:continue
