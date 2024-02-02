import pygame
pygame.init()
win = pygame.display.set_mode((400, 400))
bg=pygame.image.load('bg.png')
class Player1:
    def __init__(self):
        self.x = 10
        self.y = 300
        self.vel = 5
        self.shot=False
        self.bulletx=self.x
        self.bullety=self.y
        self.health=50
    def draw(self):
        pygame.draw.rect(win,('red'),(self.x,self.y,40,60))
        pygame.draw.rect(win, ('red'), (self.x - 5, self.y - 10, self.health, 5))

    def shoot(self):
        if self.shot:
            pygame.draw.rect(win,('red'),(self.bulletx,self.bullety+20,10,5))
            if self.bulletx < 400:
                self.bulletx+=10
            else:
                self.bulletx=self.x
                self.bullety=self.y
                self.shot=False


class Player2():
    def __init__(self):
        self.x =350
        self.y = 300
        self.vel = 5
        self.shot=False
        self.bulletx=self.x
        self.bullety=self.y
        self.health=50
    def draw(self):
        pygame.draw.rect(win,('blue'),(self.x,self.y,40,60))
        pygame.draw.rect(win,('blue'),(self.x-5,self.y-10,self.health,5))

    def shoot(self):
        if self.shot:
            pygame.draw.rect(win,('blue'),(self.bulletx,self.bullety+20,10,5))
            if self.bulletx >0 :
                self.bulletx+=-10
            else:
                self.bulletx=self.x
                self.bullety=self.y
                self.shot=False

player=Player1()
enemy=Player2()
true = True
font=pygame.font.SysFont('areiel',30)

def hit():
    if player.bullety in range (enemy.y-20,enemy.y+60) and player.bulletx in range (enemy.x,enemy.x+40):
        player.bulletx = player.x
        player.bullety = player.y
        enemy.health-=5
        player.shot=False
    if enemy.bullety in range(player.y-20, player.y + 60) and enemy.bulletx in range(player.x,player.x+40):
        enemy.bulletx = enemy.x
        enemy.bullety = enemy.y
        player.health-=5
        enemy.shot=False
def game():

    win.blit(bg,(0,0))
    if player.health >0:
        player.draw()
        player.shoot()
    else:
        win.blit(font.render('BLUE WINS!!',300,'white'),(140,150))
    if enemy.health>0:
        enemy.draw()
        enemy.shoot()
    else:
        win.blit(font.render('RED WINS!!', 300, 'white'), (140, 150))
    hit()
    pygame.display.update()

while true:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False

    key = pygame.key.get_pressed()
    #player1
    if key[pygame.K_w] and player.y>0:
        player.y-=player.vel
    if key[pygame.K_s] and player.y <340:
        player.y+=player.vel
    if key[pygame.K_d]:
        player.shot=True

    #player2
    if key[pygame.K_UP] and enemy.y>0:
        enemy.y-=enemy.vel
    if key[pygame.K_DOWN] and enemy.y <340:
        enemy.y+=enemy.vel
    if key[pygame.K_LEFT]:
        enemy.shot=True

    game()
pygame.quit()
