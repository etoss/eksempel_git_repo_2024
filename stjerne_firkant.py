# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:43:11 2024

@author: Erlend Tøssebro
"""

# Eksempel på funksjon med tre parametre: Firkant av tegn som
# en funksjon

def stjerne_firkant(hoyde, bredde, tegn="*"):
    """ Skriver ut en firkant i terminalen lagd av et oppgitt tegn. """
    for y in range(hoyde):
        for x in range(bredde):
            print(tegn, end="")      # end="" for å ikke få newline på slutten
        print()


# Kode som demonstrerer funksjonen
stjerne_firkant(5,4, "#")
hoyde = int(input("Skriv inn høyde: "))
bredde = int(input("Skriv inn bredde: "))
stjerne_firkant(hoyde, bredde)
stjerne_firkant(tegn="o", bredde=7, hoyde=3)
stjerne_firkant(tegn="+", bredde=4, hoyde=7)
