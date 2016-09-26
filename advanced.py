L=['Michael','Sarah','Tracy','Bob','Jack']
print([L[0], L[1], L[2]])
r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
L=list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])