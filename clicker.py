import random
import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 1000,800

screen=pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Clicker Game")

options=["New Game","Exit"]

option_selected=0
font = pygame.font.Font(None, 36)

def draw():
    screen.fill("WHITE")
    text=font.render("Welcome to the Game!!!",True,"BLACK")
    screen.blit(text,(WIDTH//2-text.get_width()//2,150))

    for i in range(len(options)):
        if option_selected==i:
            color="GREEN"
        else:
            color="BLACK"
        text=font.render(options[i],True,color)
        screen.blit(text,(WIDTH//2-text.get_width()//2,300+i*60))
    
    pygame.display.flip()

def start_home_page():
    global option_selected
    running=True
    while running:
        draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if  event.key==pygame.K_DOWN:
                    option_selected=(option_selected+1)%len(options)
                elif event.key==pygame.K_UP:
                    option_selected=(option_selected-1)%len(options)
                elif event.key==pygame.K_RETURN:
                    if option_selected==0:
                        running=False
                    elif option_selected==1:
                        pygame.quit()
                        sys.exit()

start_home_page()



x=WIDTH//2
y=HEIGHT//2

start=pygame.time.get_ticks()
score=0
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if image.collidepoint(event.pos):
                x=random.randint(0,WIDTH)
                y=random.randint(0,HEIGHT)
                score+=1
            
    seconds=(pygame.time.get_ticks()-start)/1000
    if seconds>=10:
        print("Time's up!!!, Your score is: ", score)
        running=False
    #draw
    screen.fill("WHITE")
    image=pygame.draw.circle(screen,(255,0,0),(x,y),50)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: "+str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))




    pygame.display.flip()
    



