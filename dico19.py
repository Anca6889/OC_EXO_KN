x= {"key": "valeur", "key2": "valeur2"}
print(x.get("key"))

x["titi"] = "toto"
print(x)

x["tata"] = x.pop("titi")
print(x)

del x["tata"]
print(x)


y = x
print(y)
