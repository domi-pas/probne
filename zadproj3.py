def zamiana_liter(łańcuch):
    łańcuch_zmieniony = ""
    łańcuch_zmieniony += łańcuch[-1]
    łańcuch_zmieniony += łańcuch[1:-1]
    łańcuch_zmieniony += łańcuch[0]
    return łańcuch_zmieniony


kwiat = "storczyk"
otrzymane = zamiana_liter(kwiat)
print(otrzymane)

zwierzę = "słoń"
otrzymane2 = zamiana_liter(zwierzę)
print(otrzymane2)

owoc = "banan"
otrzymane3 = zamiana_liter(owoc)
print(otrzymane3)
