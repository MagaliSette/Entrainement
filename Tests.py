# 1 - Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est nul,\n
# négatif ou positif.

premier_nombre=float(input("Quel est votrepremier nombre\n"))
deuxieme_nombre=float(input("Quel est votre deuxième nombre \n"))

total=premier_nombre*deuxieme_nombre
if total < 0:
  print("Votre résultat est négatif")
elif total > 0:
    print("Votre résultat est positif")
else :
    print("Votre résultat est nul")

# 2 - Ecrire un programme qui demande l'age de l'utilisateur, et qui lui dit s'il est majeur ou non

age=int(input("Quel âge avez vous ?\n"))

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")


# 3 - Demandez un nombre à un utilisateur, créer une condition qui affichera si le nombre de l'utilisateur est\n
# comprit entre 5 et 10. 5 et 10 sont exclut (les nombres doivent donc etre 6, 7, 8 ou 9 pour que le programme\
# afficher "vrai")

nombre=int(input("Quel est votre nombre entre 0 et 10 ?\n"))

if nombre > 5 and nombre < 10:
    print("Vrai, votre nombre est dans l'intervalle.")
else:
    print("Faux,votre nombre n'est pas dans l'intervalle.")


# 4 - Même exercice qu'avant, mais cette fois écrire la condition d'une manière différente

nombre=int(input("Quel est votre nombre entre 0 et 10 ?\n"))

if nombre > 5 and nombre <10:
    True
    print("Votre nombre est dans l'intervalle.")

else:
    False
    print("Votre nombre n'est pas dans l'intervalle.")


