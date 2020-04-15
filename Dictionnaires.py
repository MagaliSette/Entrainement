# 19 - Créer un dictionnaire "x" avec les clés / valeurs suivantes :

x={}
x["chaussures"]=3
x["chemises"]=5
print(x)


x["chaussures"]

x["toto"]="titi"
print(x)

x["toto"]="tata"
print(x)

del x["toto"]
print(x)

x.pop("chaussures")

print(x)

y={}
y=x
print(y)

