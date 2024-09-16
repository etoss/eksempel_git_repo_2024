# Importerer pakken "turtle" for å bruke Turtle Graphics
import turtle

# Viser import av math-pakken, som ikke brukes og derfor egentlig ikke
# burde importeres her
import math


turtle.pencolor("orange")   # Setter tegnefargen lik oransje
turtle.pensize(5)           # Setter penna sin bredde lik 5 piksler
turtle.fillcolor("green")   # Setter fyllfarge til grønn
turtle.begin_fill()         # Start å tegne figur som skal fylles
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()           # Figuren som skal fylles er ferdig, fyll den.

turtle.done()               # Lar turtle-vinduet være åpent selv om scriptet
                            # er ferdig.

# Kan spesifisere farger med enten vanlige fargenavn på engelsk eller 
# med et #-tegn etterfulgt av seks heksadesimale siffer. De to første
# sifrene er for rød, de to neste for grønn og de to siste for blå.
# Alle farger det menneskelige øyet kan se kan lages med en kombinasjon
# av rødt, grønt og blått. Så #FF4488 er en farge med maksimal
# verdi for rød (255), litt men ikke mye grønn, og en del men godt unna maks
# for blå.
