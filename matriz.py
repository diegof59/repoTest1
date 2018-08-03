#Matriz transpuesta
f=int(input('Digite el numero de filas y el numero de columnas: '))

#creamos una matriz vacia
A=[]
for i in range(f):
    A.append([0]*f)

#leemos su contenido de teclado

for i in range(f):
    for j in range(f):
        A[i][j]=int(input('Digite el contenido de %d y %d de la matriz A: '%(i+1,j+1)))

print('A=',A)

B=[]
for i in range(f):
    B.append([0]*f)

#leemos su contenido de tecleado

for i in range(f):
    for j in range(f):
        B[i][j]=A[j][i]
print('B=',B)
