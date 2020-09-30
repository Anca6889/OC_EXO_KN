
number_1 = input("entrer un premier nombre: ")
number_2 = input("entrer un deuxième nombre: ")

x = (int(number_1)* int(number_2))
print("le résultat du produit de ces deux nombres est: " + str(x))

if x > 0:
    print("le résultat du produit de ces deux nombres est positif")
elif x < 0: 
    print("le résultat du produit de ces deux nombres est négatif")
else:
    print("le résultat du produit de ces deux nombres est nul")
