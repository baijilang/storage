
#+=====================正序乘法表========================+#
col=1
row=1
while True:
    if row<10:
        if row>col:
            mul=row*col
            print("%d * %d = %-2d"%(col,row,mul),end='  ')
            col+=1
        elif row==col:
            print("%d * %d = %-2d" % (col, row, row*col))
            col=1
            row+=1
    else:
        break

#+=====================逆序乘法表========================+#
# col=1
# row=9
# while True:
#     if row>0:
#         if col < row  :
#             print("%d * %d = %-2d"%(col,row,col*row),end='  ')
#             col+=1
#         elif col==row:
#             print("%d * %d = %-2d" % (col, row, col * row))
#             col=1
#             row-=1
#     else:
#         break