

col=1
while True:
    row=1
    if row<10:
        if row>=col:
            mul=row*col
            print("%d*%d=%d"%(col,row,mul),end='')
            col+=1
        
