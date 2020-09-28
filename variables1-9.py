age = 30; name = "Max"

sentence = "Je suis "+ str(name) +" et j'ai " + str(age) + " ans"
print(sentence)
print("Mon age x4 est égale à " + str(age*4))
print("Mon age -1 est égale à " + str(age-1))

resultadd = input("Ajoute une valeur à mon age: ")
print(int(age) + int(resultadd))

resultsou = input("Soustrait une valeur à mon age: ")
print(int(age) - int(resultsou))

resultmul = input("Multiplie mon age par une valeur: ")
print(int(age) * int(resultmul))

resultdiv = input("Divise mon age par une valeur: ")
print(int(age) / int(resultdiv))
