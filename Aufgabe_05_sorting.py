"""
TU Berlin
Einführung in die Informationstechnik für Ingenieure

Vorgaben zu Aufgabe 05 - Kontrollstrukturen II
"""

mix = [51, 0, "Q", "LISTE", 4.3, {"null" : 0, "eins" : 1, "zwei" : 2}, -1, "Tupel", 1, "False", 3 > 5, "hell", 666, "dictionaries", True, 42.42]

# START TODO ###################

ints = []
doubles = []
strings = []
dicts = []
summe = []
# 
for val in mix:
   
    if val is type(bool): # auf boolean prüfen
        break            # laut Aufgstellung Schleife abbrechen
    elif val is type(int): # auf interger prüfen
        ints = ints.append[val]    # zu ints[] hinzufügen
    
    elif val is type(float): # auf doubles prüfen
        doubles = doubles.append[val]
        # zu doubles[] hinzufügen

    elif val is type(str): # auf strings prüfen
        strings = strings.append[val]
        # zu strings[] hinzufügen

    elif val is type(dict): # auf dictionaries prüfen
        dicts = dicts.append[val]
        # zu dicts[] hinzufügen
    
        # ... alle strings und floats zusammenaddieren

    


# END TODO #####################


# Ausgaben der Listen
print("Sortierte Listen: ")
print(ints)
print(doubles)
print(strings)
print(dicts)

# Ausgabe der Summe von allen eingelesenen Zahlen
print(summe)