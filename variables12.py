#rentrer PUHT et QUANTITE articles
items_unit_prices = input("indiquer le prix unitaire HT de l'article: ")
items_quantity = input("indiquer le nombre d'articles dans votre panier: ")

#Calcul et affichage du TOTAL HT, TVA et TOTAL TTC
items_total_ht = float(items_unit_prices) * int(items_quantity)
print("TOTAL HT: " + str(items_total_ht) + " EUR")

items_TVA_value = items_total_ht / 100 * 20
print("VALEUR TVA: "+ str(items_TVA_value) + " EUR")

items_TTC_value = items_total_ht + items_TVA_value
print ("VALEUR TTC: " + str(items_TTC_value) + " EUR")