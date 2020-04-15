# 1 - créez une boucle for qui affiche les numéros de 0 à 5

numeros=0,1,2,3,4,5
for x in numeros:
    print(x)

# 2 - créez une liste de 3 mots. Parcourez la liste a l'aide d'une boucle "for" et pour chaque mot afficher le \
# nombre de caractère du mot et le mot en question

list1=["Bonjour", "Hello", "Salut"]
list2=["Chemises", "chaussures", "pantalon"]
list3=["pommes", "poires", "orange"]

for mots in list1:
    print("longueur de la chaine", mots, "=", len(mots))

for mots in list2:
    print("longueur de la chaine", mots, "=", len(mots))

for mots in list3:
    print("longueur de la chaine", mots, "=", len(mots))

#  Soit la variable x = "anticonstitutionnellement". A l'aide d'une boucle for, afficher les lettres présentes dans x.

x = "anticonstitutionnellement"
for lettre in x:
    print(lettre + "*",end ='')

# Soit la liste suivante : x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. parcourez l'ensemble pour afficher tous les nombres

x1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for nbr in range(3):
    print(x1[nbr])


# 5 - Soit la liste suivante : x = [1,10,20,30,40,50]. Définissez a et b, 2 variables prenant chacune la sommu des\n
# nombres de la liste x. Les 2 sommes doivent être calculées différemment. Afficher a et b

x2= [1,10,20,30,40,50]
a=sum(x2)
print(a)

b = 0
for i in x2:
    b +=i
    print(b)

# 6 - En utilisant la fonction range(), afficher tous les nombres de 0 à 5 en ordre décroissant

for i in range(5, 0, -1):
    print(i)

# 7 - Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois que\
# le chiffre 3 est affiché

for i in range(1, 10):
    print(i)
    if i >=3:
        break


# 8- Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois que\
# le chiffre 3 est affiché



 # c'est pas fini car pas trouvé le solution.

# 9 - Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 9. La boucle ne doit pas afficher le nombre\
# 3" mais doit obligatoirement continuer jusqu'au bout. Le faire de 2 manières différentes"