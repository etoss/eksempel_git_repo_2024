# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:43:11 2024

@author: Erlend Tøssebro
"""

# Lag en firkant av stjerne hvor brukeren skriver inn
# høyde og bredde

hoyde = int(input("Skriv inn høyde: "))
bredde = int(input("Skriv inn bredde: "))

for y in range(hoyde):
    for x in range(bredde):
        print("*", end="")      # end="" for å ikke få newline på slutten
    print()
