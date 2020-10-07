class Carré:
    """Classe définissant un carré par:
    - son coté en cm"""

    #Attributs carré:
    def __init__(self, side, count): 
        """Attribut coté"""
        self.coté = side
        self.unités = count
        print("Bienvenue au carré de coté", side, "cm")

    #Méthodes carré:
    def get_side(self):
        return self.coté

    def get_perimeter(self):
        return self.coté*4
    
    def get_area(self):
        return self.coté*self.coté
    
    def get_factor(self):
        return self.coté*int(input("Entrer un facteur d'agrandissement: "))
    
    def get_count(self):
        return self.unités


#Lancement du programme:     

print("...")
print("Lancement du programme de définition d'un carré dans 3, 2, 1...")
input("Bienvenue dans notre de centre de création de carrés. Je suis ravis de vous voir. Appuyer sur ENTER pour continuer.")
print("...")
print("Créons ensemble un premier carré, veuillez me donner une longueur afin que je définisse son coté...")
print("...")
#Paramétrage du premier carré:

carré1 = Carré(int(input("Entrer une longueur de base en cm qui déinira le coté du carré: ")), int(input("Combien voulez vous que je crée de carrés comme celui_ci ?")))
print("Coté du carré: ", carré1.get_side(), "cm")
print("Le perimètre de ce carré est de", carré1.get_perimeter(), "cm")
print("La surface de ce carré est de", carré1.get_area(),"cm2")
print("Nombre de carrés de ce type: ", carré1.get_count(), "unité(s)")
print("...")

input("A présent je vais créer un deuxième carré à partir d'un facteur d'agrandissement de ce même carré, appuyer sur ENTER pour continuer...")
#Création d'un deuxième carré avec un facteur d'agrandissement du premier:

carré2 = Carré(carré1.get_factor(), 1)
print("Le nouveau coté de ce carré est de: ", carré2.get_side(), "cm")
print("Ce carré est", int(carré2.get_side()/carré1.get_side()) , "fois plus grand que le précédent" )
print("Le perimètre de ce carré est de", carré2.get_perimeter(), "cm")
print("La surface de ce carré est de", carré2.get_area(), "cm2")
print("...")

input("Maintenant je vais additionner ces deux carrés ensemble, appuyer sur ENTER pour continuer...")

#Création d'un troisième carré qui à pour coté l'addition des deux cotés des deux carrés précédents:

carré3 = Carré(carré1.get_side()+carré2.get_side(), 1)
print("Le premier carré avait un coté de", carré1.get_side(), "cm et le deuxième carré avait un coté de", carré2.get_side(), "cm")
print("Le nouveau coté de ce carré est de: ", carré3.get_side(), "cm")
print("Ce carré est", float(carré3.get_side()/carré2.get_side()), "fois plus grand que le précédent")
print("Le perimètre de ce carré est de", carré3.get_perimeter(), "cm")
print("La surface de ce carré est de", carré3.get_area(), "cm2")
print("...")


input("Maintenant je vais soustraire 1 cm à ce dernier carré, appuyer sur ENTER pour continuer...")

#Création d'un quatrième carré qui à pour coté la soustraction de 1cm du coté du troisième carré:

carré4 = Carré(carré3.get_side()-1, 1)
print("Le dernier carré avait un coté de", carré3.get_side(), "cm")
print("Le nouveau coté de ce carré est de: ", carré4.get_side(), "cm")
print("Ce carré est", float(carré3.get_side()/carré4.get_side()),"fois plus petit que le précédent")
print("Le perimètre de ce carré est de", carré4.get_perimeter(), "cm")
print("La surface de ce carré est de", carré4.get_area(), "cm2")
print("...")

def comparefunction():
    print("Lancement du sous-programme de comparaison des carrés")

    compare_high = carré4.get_side() > carré3.get_side()
    print("Le carré4 est t'il plus grand que le carré3 ? ", compare_high)
    compare_low = carré4.get_side() < carré3.get_side()
    print("Le carré4 est t'il plus petit que le carré3 ? ", compare_low)
    compare_eg_low = carré4.get_side() <= carré3.get_side()
    print("Le carré4 est t'il égal ou plus petit que le carré3 ? ", compare_eg_low)
    compare_eg_high = carré4.get_side() >= carré3.get_side()
    print("Le carré4 est t'il égal ou plus grand que le carré3 ? ", compare_eg_high)
    compare_absolute_eg = carré4.get_side() == carré3.get_side()
    print("Le carré4 est t'il égal au carré3 ? ", compare_absolute_eg)
    compare_not_eg = carré4.get_side() != carré3.get_side()
    print("Le carré4 est t'il inégal au carré3 ? ", compare_not_eg)

comparefunction()

print("Nous avons été ravis de créer des carrés avec vous. Nous en tirons une immense joie. A présent, ce programme s'arrêtera dans: ")
print("3...")
print("2...")
print("1...")


