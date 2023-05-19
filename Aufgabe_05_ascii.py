# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:29:59 2023

@author: simon
"""

print("Dieses Programm erstellt ein Rechteck aus A-Zeichen.")
print("Um das Rechteck ist ein Rahmen aus C-Zeichen.")
hoehe = int(input("Bitte Höhe eingeben: "))
breite = int(input("Bitte Breite eingeben: "))

x = 0                               # Position des Buchstabens in x-Richtung
y = 0                               # Position des Buchstabens in y-Richtung

print("C" * (breite + 2) + "\n", end=('')) # erste Zeile des Rechtecks
while y < hoehe:                    # Start Mittelteil
    print("C", end=(""))            # Linker Rahmen 
    while x < breite:               # Mittelteil mit As
        print("A", end=(''))        
        x += 1
    print("C")                      # Rechter Rahmen und Zeilensprung
    x = 0                           # Neu beginnen ganz links
    y += 1
print("C" * (breite + 2) + "\n", end=('')) # letzte Zeile des Rechtecks