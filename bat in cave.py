import pygame,random,sys,time
pygame.init()
clock=pygame.time.Clock()
X,Y=1100,900
screen= pygame.display.set_mode((X,Y))
pygame.display.set_caption("First Game")
bat= pygame.image.load('bat0.png')
bat=pygame.transform.scale(bat,(100,60))
bat_rect = bat.get_rect(center=(550,380))

background=pygame.image.load('background2.png')
Q=13
p_rects=[0]*Q

img=['stm1.png','stm1.png','stc1.png','stm2.png','stc2.png',\
     'stm1.png','stc1.png','stm2.png','stc2.png',\
     'stm1.png','stc1.png','stm2.png','stc2.png',\
     'line.png']

lines_rect=[0]*Q
line2_rect=pygame.Rect(540,350,5,60)
platform=[]
posx=[X//2,140,150,355,300,520,460,670,670,860,860,1010,1020,548]
posy=[5*Y,   900,350,950,450,980,450,950,450,900,350,960,450,750]

posx1=[X//2,130,150,345,300,510,460,660,670,845,860,1000,1015,548]
posy1=[Y,  245,20,290,80,330,120,300,80,250,20,310,85,950]
for i in range(Q):
    platform.append(pygame.image.load(img[i]))
collision=0
eps=0
ingame=False
start_image=pygame.image.load('start1.png')
def start():
    global Time,eps,ingame,start_time,Sum
    eps=0
    start_rect=start_image.get_rect(center=(750,850))
    screen.blit(start_image,start_rect)
    if pygame.mouse.get_pressed()[0] == 1:
        start_time = pygame.time.get_ticks()
        Time=0
        Sum=0
        ingame=True            
def times():
    global Time,eps,ingame,start_time,finish_time
    if ingame  and Time<=finish_time:
        eps=5
        Time= (pygame.time.get_ticks() - start_time)//1000
        text=font.render(str(Time),True,'blue')
        screen.blit(text,(900,50))
    if Time>finish_time:
        eps=0
        text=font.render(str(Time),True,'blue')
        screen.blit(text,(1900,50))
def move():
    for i in range(1,Q):
        posx[i]=posx[i]+eps
        posx1[i]=posx1[i]+eps
        if posx[i]>=1100:
            posx[i]=posx[i]-1100
            posx1[i]=posx1[i]-1100
k=0
Sum=0
finish_time=40
Time=0
font=pygame.font.Font(None,70)
while True:
    screen.fill('grey')
    screen.blit(background,(0,0))
    k=k+1
    k1=k%18
    if k1<=9:
        bat= pygame.image.load('bat0.png')
    if k1>9:
        bat= pygame.image.load('bat1.png')
    if Time>=finish_time:
        bat= pygame.image.load('bat0.png')
    bat=pygame.transform.scale(bat,(72,43))
    #pygame.draw.rect(screen,'blue',line2_rect)#!!!!!!!!!!!!!!!!!!!!!!!!!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        line2_rect.y=line2_rect.y-5
        bat_rect.centery-= 5
    if keys[pygame.K_DOWN]:
        line2_rect.y=line2_rect.y+5
        bat_rect.centery+= 5
    move()
    for i in range(1,Q):
        p_rects[i]=platform[i].get_rect(midbottom=(posx[i],posy[i]))
        screen.blit(platform[i],p_rects[i])
        lines_rect[i]=pygame.Rect(posx1[i],posy1[i]+100,5,150)
        #pygame.draw.rect(screen,'blue',lines_rect[i])#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        collision=line2_rect.colliderect(lines_rect[i])
        if collision!=0:
            Sum=Sum+1
    if Time>finish_time:
        text2=font.render('Number of collisions=',True,'blue')
        screen.blit(text2,(150,350))
        text3=font.render(str(Sum),True,'blue')
        screen.blit(text3,(700,350))
    p_rects[0]=platform[0].get_rect(midbottom=(posx[0],posy[0]))
    screen.blit(platform[0],p_rects[0])
    screen.blit(bat,bat_rect)
    start()
    times()
    clock.tick(150)   
    pygame.display.update()