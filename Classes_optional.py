import random

class Fighter:
    """Classe définissant un combattant par:
    - son nom
    - son sexe
    - sa nationalité
    - sa taille en cm
    - son poids en kg
    - sa vie en PV
    - sa vitesse par une liste de facteurs multiplicateurs d'attaque
    - son attaque en point de dommage
    - sa défense en point de défense
    - sa vie maximum (crée pour afficher des dommages)
    - son style de combat """

#attributs Fighter:
    def __init__(self, name, sexe, nationality, size, weight, health, speed, attack, defense, maxhealth, style):
        self.name = name
        self.sexe = sexe
        self.nationality = nationality
        self.size = size
        self.weight = weight
        self.health = health
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.maxhealth = maxhealth
        self.style = style
        
        
        print("Welcome to fighter", name, "master in", style, "!")
        
#Méthodes Fighter
    def get_name(self):
        return self.name

    def get_sexe(self):
        return self.sexe

    def get_nationality(self):
        return self.nationality

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def get_health(self):
        return self.health

    def get_speed(self):
        return self.speed

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_maxhealth(self):
        return self.maxhealth

    def get_style(self):
        return self.style

    # Méthode d'encaissement des dommages, modifie la santé du fighter.
    # Fonctionne avec l'attaque de l'adversaire et les points de défense.
    def damage(self, damage):
        self.health -= damage - self.defense

    # Méthode d'attaque d'un adversaire. Designe une cible qui inflige des dégats.
    # Fonctionne avec la méthode damage, points d'attaque et facteur de vitesse.
    def hit_ennemy(self, target):
        target.damage(self.attack*random.choice(self.speed))

    # Méthode créee pour afficher les dommages lors d'un combat:
    def new_max_health(self):
        self.maxhealth = self.health

#Lancement du programme:
print("...")
print("Welcome to our great fighting tournament !")
input("Please welcome our amazing fighters !!! Press ENTER to continue")
print("...")

#Combattants:
fighter1 = Fighter("Anca", "male", "French", 175, 72, 125, [1,2,3], 16, 5, 125, "Nimpo tai-ju-tsu")
fighter2 = Fighter("Saber", "female", "French", 155, 55, 110, [1,2,3,4,5], 11, 2, 110, "Katana-Kenjutsu")
fighter3 = Fighter("General Valeri Guerassimov", "male", "Russian",187, 95, 140, [1,2], 25, 10, 145, "Cистема")
fighter4 = Fighter("Peter", "male", "British", 185, 90, 135, [1,2], 23, 8, 135, "Pub fighting")
fighter5 = Fighter("Ashley", "female", "American", 165, 60, 115, [1,2,3], 14, 3, 115, "Karate shotokan")
fighter6 = Fighter("Ricardo Augusto Ferreira Costa Neves", "male","Brazilian", 170, 69, 120, [1,2,3,4], 12, 4, 120, "Brazilian jiu jitsu ")

#Placement des combattants dans une liste pour les sélectionner au hasard:
listfighters = [fighter1, fighter2, fighter3, fighter4, fighter5, fighter6]

#Lancement du premier combat:
print("...")
print(" for the first battle, please take position: ")
print("...")

first_fighter = random.choice(listfighters)
second_fighter = random.choice(listfighters)


print(first_fighter.get_name(), "VS", second_fighter.get_name())
input("Press enter to continue ")
print("...")
print("let us compare our amazing fighters: ")
print("...")
print("Fighters:___",first_fighter.get_name(), "_____VS_____", second_fighter.get_name())
print("Sexe:_______",first_fighter.get_sexe(), "_____VS_____", second_fighter.get_sexe())
print("Nationality:", first_fighter.get_nationality(), "_____VS_____", second_fighter.get_nationality())
print("Size:_______", first_fighter.get_size(),"cm","_____VS_____", second_fighter.get_size(),"cm")
print("Weight:_____", first_fighter.get_weight(), "kg","_____VS_____", second_fighter.get_weight(), "kg")
print("Style:______", first_fighter.get_style(),"_____VS_____", second_fighter.get_style())

#Début du premier combat:
print("...")
input("Ready to fight ? Press ENTER to Fight!")
print("...")

while first_fighter.get_health() or second_fighter.get_health() >= 0:

    first_fighter.hit_ennemy(second_fighter)
    print(first_fighter.get_name(), "attack", second_fighter.get_name(),"and inflate", second_fighter.get_maxhealth() - second_fighter.get_health(), "PV damage")
    print(second_fighter.get_name(), "have", second_fighter.get_health(), "PV remain")
    print("...")
    second_fighter.new_max_health()

    second_fighter.hit_ennemy(first_fighter) 
    print(second_fighter.get_name(), "attack", first_fighter.get_name(), "and inflate",first_fighter.get_maxhealth() - first_fighter.get_health(), " PV damage")
    print(first_fighter.get_name(), "have", first_fighter.get_health(), "PV remain")
    print("...")
    first_fighter.new_max_health()

    if first_fighter.get_health() <= 0:
        print(first_fighter.get_name(), "is KO ! The winner is",second_fighter.get_name(), "!!!")
        break

    elif second_fighter.get_health() <=0:
        print(second_fighter.get_name(), "is KO ! The winner is", first_fighter.get_name(), "!!!")
        break


