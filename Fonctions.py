# 1 - Définir une fonction qui prends un nombre en paramètre et le multiplie par 5. Afficher le résultat

def mult(m5):
    m5=m5*5
    return m5

print(mult(2))

# 2 - Définir une fonction qui prend une liste de nombres en paramètre et qui retourne tous les nombres pairs


list1=[1, 5, 8, 10, 11, 15, 17, 20]

def listnbr(*list1):
    for listnbr in range(list1, 2):
        print(listnbr)
    return


# 3 - Définir une fonction qui écrit la suite de fibonacci, et prend en paramètre un nombre. La fonction n'ira pas\
# plus loin que ce nombre.

def fibonacci(m):
    if(m <=1):
        return m
    else:
        return (fibonacci(m-1) + fibonacci(m-2))

m= int(input("Entrez le nombre de termes:"))

print("Voici la suite")
for i in range(m):
    print(fibonacci(i))

# 4 - Définir une fonction qui compte le nombre de voyelle dans une chaine de caractère passé en argument avec une\
# boucle for. Définir une deuxième fonction identique avec une boucle while. En faire une troisième avec une\
# string dans le "in" de la condition



# 5 - Définir une fonction qui retourne la factorielle d'un nombre passé en argument. Par rappel, la factorielle \
# d'un nombre "n" et la multiplication de tous les nombres n par les nombres n-1 jusqu'à ce que n soit égal à 1.

def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n  * factorielle(n-1)



# 6 - Recommencer une fonction de factorielle de n avec une fonction récurrente

def recursivite(nb):
    if nb > 2:
        return nb * recursivite(nb - 1)
    return nb

# 7 - Définir une fonction avec une nombre variable d'arguments. La fonction devra afficher le nombre d'arguments \
# passer, et la somme des nombres (qui seront donc passés en arguments)

def arguments(x=0, y=0, z=0):
    return x, y , z


arguments(z=4)


# 8 Soit la liste suivante : [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]. Définir une fonction permettant de récupérer\
# le premier chiffre d'un nombre. créer une deuxième fonction qui appelle la première pour afficher la fréquence \
# d'apparition des premiers chiffres.

liste1 = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]

def premier_nombre(n):
    liste1 = str(n)
    if len(liste1) != 1:
        return n

