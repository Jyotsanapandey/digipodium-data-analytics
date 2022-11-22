import pgzrun
HEIGHT = 300
WIDTH = 800
p = Actor('ironman',(200,100))
c = Actor('cookie_img') 

def draw():
    screen.fill('white')
    p.draw()
    c.draw()

pgzrun.go()