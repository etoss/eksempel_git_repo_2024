# Importerer pakken "turtle" for å bruke Turtle Graphics
import turtle

# Viser import av math-pakken, som ikke brukes og derfor egentlig ikke
# burde importeres her
import math


def tegn_trekant(pennstorrelse = 5, pennfarge="orange", fyll="green"):
    turtle.pencolor(pennfarge)   # Setter tegnefargen lik oransje
    turtle.pensize(pennstorrelse)# Setter penna sin bredde lik 5 piksler
    turtle.fillcolor(fyll)   # Setter fyllfarge til grønn
    turtle.begin_fill()         # Start å tegne figur som skal fylles
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()           # Figuren som skal fylles er ferdig, fyll den.


tegn_trekant()
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
tegn_trekant(3, "black", "blue")
turtle.done()               # Lar turtle-vinduet være åpent selv om scriptet
                            # er ferdig.

# Kan spesifisere farger med enten vanlige fargenavn på engelsk eller 
# med et #-tegn etterfulgt av seks heksadesimale siffer. De to første
# sifrene er for rød, de to neste for grønn og de to siste for blå.
# Alle farger det menneskelige øyet kan se kan lages med en kombinasjon
# av rødt, grønt og blått. Så #FF4488 er en farge med maksimal
# verdi for rød (255), litt men ikke mye grønn, og en del men godt unna maks
# for blå.
