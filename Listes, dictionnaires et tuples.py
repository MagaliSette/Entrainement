#  Créez une liste "x" de 4 tuples de forme (x, y)

listx=[("a","b","c","d")]

print(listx)

listx=[("a","b","c","d"),"a"]
print(listx)

listx=[("a","b","c","d"),"a"]
listx.insert(2,"b")
print(listx)

listy=[1, 2, 3]
listx.extend(listy)
print(listx)

listx.insert(4,2)
print(listx)

del listx[4]
print(listx)

print(listy)

listz=listy[:]
print(listz)

del listy [0]
del listy [1]
del listy [0]

print(listy)

del listz








