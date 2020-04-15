# 1 - Créez une classe "Carre", prennant en paramètre un élément "côté", représentant la longueur d'un côté en cm.

class Carre:
    def __init__(self, cote =3):
        self.cote = cote

    def getCarre(self):
        return self.cote**2

    def perimeter(self):
        return self.cote*4

    def area(self):
        return self.cote*self.cote


first_carre= Carre(5)

carre = first_carre.getCarre()
perimeter = first_carre.perimeter()
area = first_carre.area()

print("Le périmetre est de", str(perimeter), "cm, l'air est de", str (area),"cm et la longueur du côté est de",5, "cm.")


