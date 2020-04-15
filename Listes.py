# 13 - Ecrire une liste comportant les nombres "4" et "5" et l'afficher.

liste1=[4, 5]
print(liste1)

# 14 - Ecrire une liste avec 2 chaines de caractère et 2 nombres.

liste2=["Hello","World",10,5]
print(liste2)

print(liste2[0])

print(type(liste2[2]))

# 15 - Créer 2 listes "x" et "y", avec 2 nombres dans chacune d'elle. Créer une troisième liste qui sera la \n
# concaténation de x et y. Afficher cette troisième liste

x=[2,5]
y=[10, 8]
print(x+y)


# 16 - Soit la liste suivante : x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x2= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x2[3])

print(x2[3],x2[4])

print(x2[3], x2[5])

longueur=len(x2)
print(longueur)

def minimum(x2):
    mini=x2[0]
    for i in x2:
        if i <= mini:
            mini = i
        return mini

def maximum(x2):
    maxi=x2[0]
    for i in x2:
        if i >= maxi:
            maxi = i
        return maxi

sum(x2)
print(sum(x2))

del x2[4]
print (x2)
del x2[3]
print(x2)

# Soit la liste suivante : x = ["ok", 4, 2, 78, "bonjour"]

x3= ["ok", 4, 2, 78, "bonjour"]

print(x3[3])

x3[1]="toto"
print(x3)

#  Créez une liste des nombres allant de 0 à 5, le faire de 2 manières possible et afficher les résultats

x4=[0, 1, 2, 3, 4, 5]
print(x4)

x5=x4
print(x5)

