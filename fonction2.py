list1 = [i for i in range(100)]
print(list1)

def printpairs():
    paire = [nb for nb in list1 if not nb % 2]
    impaire = [nb for nb in list1 if not nb in paire]
    print(paire)

printpairs()
