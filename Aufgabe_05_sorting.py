"""
TU Berlin
Einführung in die Informationstechnik für Ingenieure

Vorgaben zu Aufgabe 05 - Kontrollstrukturen II
"""

mix = [51, 0, "Q", "LISTE", 4.3, {"null" : 0, "eins" : 1, "zwei" : 2}, -1, "Tupel", 1, "False", 3 > 5, "hell", 666, "dictionaries", True, 42.42]

# START TODO ###################

# Definiere die Sortierten Listen und Variablen
ints = []
doubles = []
strings = []
dicts = []
summe = 0

for val in mix:
   
    if type(val) is bool: # auf boolean prüfen
        break            # laut Aufgstellung Schleife abbrechen
        
    elif type(val) is int: # auf interger prüfen
       ints.append(val)    # zu ints hinzufügen
    
    elif type(val) is float: # auf doubles prüfen
        doubles.append(val) # zu doubles hinzufügen
        
    elif type(val) is str: # auf strings prüfen
        strings.append(val) # zu strings hinzufügen
        
    elif type(val) is dict: # auf dictionaries prüfen
        dicts.append(val) # zu dicts hinzufügen
        
# alle strings und floats zusammenaddieren    
merged = ints + doubles    # Listen aus floats und intergers zusammenfügen     

for i, index in enumerate(merged): 
    summe += float(merged[i])      # merged in float umwandeln und der Summe hinzufügen für alle Werte in der Liste
    
# END TODO #####################


# Ausgaben der Listen
print("Sortierte Listen: ")
print(ints)
print(doubles)
print(strings)
print(dicts)

# Ausgabe der Summe von allen eingelesenen Zahlen
print(summe)