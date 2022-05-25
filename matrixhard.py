'''n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            x=i;y=j
            while(y>=0 and x<n):
                if m[x][y]!=1:
                    m[x][y]='x'
                x+=1;y-=1
            a=i;b=j
            while(a>=0 and b<n):
                if m[a][b]!=1:
                    m[a][b]='x'
                a-=1;b+=1
            x1=i;y1=j
            while(x1<n and y1<n):
                if m[x1][y1]!=1:
                    m[x1][y1]='x'
                x1+=1;y1+=1
            a1=i;b1=j
            while(a1>=0 and b1>=0):
                if m[a1][b1]!=1:
                    m[a1][b1]='x'
                a1-=1;b1-=1
c=0
for i in m:
   print(*i)
   c=c+i.count(0)
print(c)
n = int (input ())
Matrix = []
for i in range (n):
    List = list (map (int, input ().split ()))
    Matrix.append (List)

Index = []
def check (i, j):
    for x in range (n):
        for y in range (n):
            if x + y == i + j or x - y == i - j:
                Index.append ((x, y))
for i in range (n):
    for j in range (n):
        if Matrix[i][j] == 1:
            check (i, j)
print ((n * n) - len (set (Index)))
print(Matrix)'''

n = int (input ())
Matrix = []
for i in range (n):
    List = list (map (int, input ().split ()))
    Matrix.append (List)

Index = []
def check (i, j):
    for x in range (n):
        for y in range (n):
            if x + y == i + j or x - y == i - j:
                Index.append ((x, y))

for i in range (n):
    for j in range (n):
        if Matrix[i][j] == 1:
            check (i, j)
            
print ((n * n) - len (set (Index)))
Index = list (set (Index))
for i in range (n):
    for j in range (n):
        k = (i, j) in Index
        if k == False:
            Matrix[i][j] = "X"
print (Matrix)


