# 1 - Créer un script qui demande un nombre entier à l'utilisateur. Lancez une exception si l'utilisateur ne renseigne\
# pas un nombre

nombre=int(input("Veuillez saisir un nombre: \n"))
if nombre != int:
    raise ValueError
print("Ceci n'est pas un nombre, veuillez réessayer.")