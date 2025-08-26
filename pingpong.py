# program pingpong
# Wyświetlamy tło

# Wczytujemy moduł pgzrun
import pgzrun
from random import randint

# Definiujemy klasy i funkcje dodatkowe

# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

# Definiujemy wyświetlane obiekty i ich współrzędne X oraz Ypalette_a = Actor("palette.png")
palete_a = Actor("pallette")
palette_a.y = 10
palette_a.x = randint(70, 1210)
palette_b = Actor("palette")
palette_b.x = 843
palette_b.y = randint(70, 1210)
ball = Actor("ball")
ball.y = HEIGHT //2
ball.x = WIDTH //2

# Najważniejsze funkcje sterujące
def update():
    pass

def draw():
    screen.blit("nature-2384_1280", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()

# Uruchomienie modułu Pygame Zero
pgzrun.go()