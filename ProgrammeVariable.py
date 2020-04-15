# 12 Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et qui définit une variable contenant \n
# le taux de TVA à 20%, et qui fournit le prix total TTC correspondant. Se servir de la fonction "input()" pour \n
# demander a l'utilisateur de renseigner les informations.


prix_HT=float(input("Entrez le prix Hors Taxe\n"))


nombre_articles=input("Entrez le nombre d'articles\n")
nombre_articles=int(nombre_articles)

TVA=0.20

formule=(prix_HT*nombre_articles)*TVA
prix_TTC=(prix_HT*nombre_articles)-formule
print("Le prix TTC de vos achats est", prix_TTC)

