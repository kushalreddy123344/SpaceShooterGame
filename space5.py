import pygame as pg
import random
import math
import time
#initializing the pygame
pg.init()
s=pg.display.set_mode((800,600))
bg=pg.image.load('space.png')
pg.display.set_caption('spaceshooter')
icon=pg.image.load('ss.png')
pg.display.set_icon(icon)
pi=pg.image.load('ss32.ico')
px=390
py=480
pxc=0
ei=[]
ex=[]
ey=[]
exc=[]
eyc=[]
n=6
for i in range(n):
    ei.append(pg.image.load('32f.ico'))
    ex.append(random.randint(0,800))
    ey.append(random.randint(50,150))
    exc.append(1.5)
    eyc.append(5)
bi=pg.image.load('bullet.ico')
bx=0
by=480
bxc=0
byc=7
bs='letsgo'
score=0
font=pg.font.Font('freesansbold.ttf',28)
tx=10
ty=10
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
clock=pg.time.Clock()
def button(msg,x,y,w,h,c,do=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(s, green, (x,y, w, h))

        if click[0]==True and do != None:
            do()
    else:
        pg.draw.rect(s, red, (x,y, w,h))
    attack = font.render(msg, True, (0, 0, 0))
    s.blit(attack, (x+15,y+10))
def gameintro():
    intro=True
    while intro:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
        s.fill(white)
        menu=font.render('MENU',True,(0,0,0))
        s.blit(menu,(250,250))
        button("GO!",150,450,100,50,green,gameloop)
        button("QUIT!",550,450,100,50,red,quitgame)

        pg.display.update()
        clock.tick(60)



def gameover():
    game=font.render('GAME OVER',True,(255,255,255))
    s.blit(game,(250,250))
def show(x,y):
    sco=font.render('score :'+str(score),True,(255,255,255))
    s.blit(sco,(x,y))
def player(x,y):
    s.blit(pi,(x,y))
def enemy(x,y,i):
    s.blit(ei[i],(x,y))
def bullet(x,y):
    global bs
    bs='fire'
    s.blit(bi,(x+4,y+10))
def col(ex,ey,bx,by):
    distance=math.sqrt(math.pow((ex-bx),2)+math.pow((ey-by),2))
    if distance<27:
        return True
    else:
        return False
def quitgame():
    pg.quit()
    quit()

#s stands for screen
def gameloop():

    global px,py,pxc,pyc,bs,by,byc,bxc,bx,score
    run=True
    while run:
        s.fill((0, 0, 0))
        s.blit(bg,(0,0))
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_LEFT:
                    pxc=-5
                if event.key==pg.K_RIGHT:
                    pxc=5
                if event.key==pg.K_SPACE:
                    if bs=='letsgo':
                        bx=px
                        bullet(bx,by)
            if event.type==pg.KEYUP:
                if event.key==pg.K_LEFT or event.key==pg.K_RIGHT:
                    pxc=0
        px+=pxc
        if px<=0:
            px=0
        elif px>=764:
            px=764
        for i in range(n):
            if ey[i]>440:
                for j in range(n):
                    ey[j]=2000
                gameover()
                break
            ex[i]+= exc[i]
            if ex[i]<= 0:
                exc[i]= 4
                ey[i]+=eyc[i]
            elif ex[i]>= 764:
                exc[i]= -4
                ey[i]+=eyc[i]
            coll = col(ex[i], ey[i], bx, by)
            if coll:
                by = 480
                bs = 'letsgo'
                score += 1
                ex[i]= random.randint(0, 800)
                ey[i]= random.randint(50, 150)
            enemy(ex[i],ey[i],i)
        if by <= 0:
            by=480
            bs='letsgo'
        if bs=='fire':
            bullet(bx,by)
            by-=byc
        player(px,py)
        show(tx,ty)
        pg.display.update()
        clock.tick(60)
gameintro()
gameloop()