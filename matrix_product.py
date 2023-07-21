def mat_pro(matrix,r,c,a):
    res=[]
    for i in range(0,r):
        rows=[]
        for j in range(0,c):
            num=matrix[i][j]*a
            rows.append(num)
        res.append(rows)    
    return res       
    

matrix=[]
a=int(input())
r,c=map(int,input().split())
for i in range(0,r):
    row=[]
    for j in range(0,c):
        element=int(input((f'{i},{j}: ')))
        row.append(element)
    matrix.append(row)
print(mat_pro(matrix,r,c,a))    

