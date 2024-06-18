import turtle
import time
import random
import math

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=700,height=700)
wn.tracer(0)
wn.title("MAZE RUNNER BY @AANYA")

turtle.register_shape("hunter (1).gif")
turtle.register_shape("/Users/aanyasingh/Desktop/maze runner/invader.gif")
turtle.register_shape("/Users/aanyasingh/Desktop/maze runner/enemy.gif")
#white cubes maze
Pen=turtle.Turtle()
Pen.shape("square")
Pen.color("grey")
Pen.speed(0)
Pen.penup()
        
#player
player=turtle.Turtle()
player.shape("/Users/aanyasingh/Desktop/maze runner/enemy.gif")
player.color("blue")
player.speed(0)
player.penup()
player.direction="stop"

#treasur
treasure=turtle.Turtle()
treasure.speed(0)
treasure.shape("hunter (1).gif")
treasure.color("gold")
treasure.penup()

#
go=turtle.Turtle()
go.speed(0)
go.penup()
go.shape("square")
go.color("white")
go.hideturtle()
# go.goto(0,0)
# go.shapesize(20,20)

#walls
wall=[""]
enemies=[]

#enemies
class enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("/Users/aanyasingh/Desktop/maze runner/invader.gif")
        self.color("purple")
        self.penup()
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
    def move(self):
        if self.direction=="up":
            mx=0
            my=24
        elif self.direction=="down":
            mx=0
            my=-24
        elif self.direction=="left":
            mx=-24
            my=0
        elif self.direction=="right":
            mx=24
            my=0
        else:
            mx=0
            my=0
     
        move_to_x=self.xcor()+mx
        move_to_y=self.ycor()+my
      
        if (move_to_x,move_to_y) not in wall:
            self.goto(move_to_x,move_to_y)
        
        else:
            self.direction=random.choice(["up","down","left","right"])
            
        turtle.ontimer(self.move,t=random.randint(100,300))

 

def go_left():
    player.direction="left"

def go_right():
    player.direction="right"

def go_down():
    player.direction="down"
    
def go_up():
    player.direction="up"

  

        
def move():
    if player.direction=="left":
        x=player.xcor()-24
        y=player.ycor()
        if(x,y) not in wall:
         player.goto(x,y)
           
    if player.direction=="right":
        x=player.xcor()+24
        y=player.ycor()
        if(x,y) not in wall:
         player.goto(x,y)
        
    if player.direction=="down":
        x=player.xcor()
        y=player.ycor()-24
        if(x,y) not in wall:
         player.goto(x,y)
        
    if player.direction=="up":
        x=player.xcor()
        y=player.ycor()+24
        if(x,y) not in wall:
         player.goto(x,y)

#keys
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_up,"Up")
 
        
levels=[""]
level_1=[                        
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X        XP X        X  X",
"X  XXXX  X  X  X  X  X  X",
"X  XE          X  X  X  X",
"X  X  XXXXXXX  XXXX  X  X",
"X  X     X  X  X  X  X  X",
"X  X  XXXX  XXXX  X  X  X",
"X  X          EX  X     X",
"XXXX  XXXXXXX  X  X  XXXX",
"X     X  X        X     X",
"XXXX  X  X  X  XXXX  XXXX",
"XE    X     X  X  X     X",
"X  XXXX  XXXXXXX  XXXXXXX",
"X     X  X     X        X",
"X  XXXXXXX  XXXX  XXXXXXX",
"X  X  X        X  X     X",
"X  X  X  X  XXXX  X  XXXX",
"X        X  XT          X",
"XXXX  X  XXXXXXX  XXXX  X",
"X     XE          X     X",
"XXXX  XXXXXXXXXXXXXXXX  X",
"X  X     X     X        X",
"X  XXXX  XXXX  XXXXXXX  X",
"X           X           X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"]
level_2=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XP XXXX  X  X EXXXXXXX  X",
"X  XXXX  X  X     X     X",
"X  XXXXXXX  X  X  XXXX  X",
"X           X  X  X     X",
"XXXXXXXXXXXXX  XXXXXXX  X",
"XE             X        X",
"XXXX  XXXX  X  X  XXXX  X",
"X     X  X  XXX   X  X  X",
"X  XXXX  XXXX  X  X  XXXX",
"X     X  X     X        X",
"XXXX EX  X  XXXX  XXXX  X",
"X     X  X  X     X     X",
"XXXX  X  X  XXXX  XXXXXXX",
"X             EX        X",
"XXXX  XXXXXXX  X  XXX  XX",
"X  X  X     X  X  X     X",
"X  XXXX  X  X  XXXXXXXXXX",
"X        XXXXE          X",
"X  X  XXXXXXXXXXXXXXXX  X",
"X  X        X  X        X",
"XXXXXXX  XXXXXXX  XXXXXXX",
"X                     ETX" ,
"XXXXXXXXXXXXXXXXXXXXXXXXX" 

]

levels.append(level_1)
levels.append(level_2)
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            ch=level[y][x]
            screen_x=-288 + (24*x)
            screen_y=288-(24*y)
            if ch=="X":
                Pen.goto(screen_x,screen_y)
                Pen.stamp()
                wall.append((screen_x,screen_y))
                
            if ch=="P":
                player.goto(screen_x,screen_y)
            if ch=="T":
                treasure.goto((screen_x,screen_y))
            if ch=="E":
                enemies.append(enemy(screen_x,screen_y))
                
# setup_maze(levels[1]) 
setup_maze(random.choice(levels))
# print(wall)
def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance<=20:
        return True;
    else:
        return False

for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)
    
delay=0.1
while True:
    wn.update() 
    if iscollision(player,treasure):
        treasure.goto(1000,1000)
        player.goto(1000,1000)
        # for enemy in enemies:
        #     enemy.goto(1000,1000)
        go.clear()
        go.write("You found the portal!!",align="center", font=("Courier",30,"normal"))
        go.showturtle()
    
    for enemy in enemies:
        if iscollision(player,enemy):
            player.goto(1000,1000)
            # for enemy in enemies:
            #     enemy.goto(1000,1000)
            treasure.goto(1000,1000)
            go.clear()
            go.write("You Lost !!",align="center", font=("Courier",30,"normal"))
            go.showturtle()
            
        
    
    move()
    # enemy_move()
    time.sleep(delay)
    
wn.mainloop()