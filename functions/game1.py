import pgzrun

WIDTH = 1200
HEIGHT = 600

scr = 0

def gamescr(bgcolor,title, info = "Play the game"):  # here we are are giving default parameter 
    screen.fill(bgcolor)
    screen.draw.text(title, center = (WIDTH/2, HEIGHT/2),fontsize = 100 , color = 'white', align = 'center')
    screen.draw.text(info, center = (WIDTH/2, HEIGHT/2+100),fontsize = 50 , color = 'white', align = 'center')

def draw():
    if scr == 0:
        gamescr('black','Amazing game','Press space to start')
    elif scr == 1:
        gamescr('blue','Game is running')
    elif scr == 2:
        gamescr('red','Game Over','Press enter to restart')    

   

def update():
    global scr
    if keyboard.space and scr == 0:
        scr = 1
    if keyboard.escape and scr == 1:
        scr = 2    
    if keyboard.RETURN and scr == 2:
        scr =0
        
pgzrun.go()