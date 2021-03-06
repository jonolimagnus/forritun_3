#jón ólafur
#lokaverkefni

import pygame
import random
import os
import sys

#hér er hægt að breyta stærðinn á rammanum
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
#hér getur þú breytt litunum á stöfunum svart er t.d 0,0,0
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Keybindings
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
FIRE = pygame.K_SPACE
QUIT = pygame.K_ESCAPE

# Config
LEIKMADUR_HRADI = 6   #hér þarftu að breyta hraðanum á leikmanninum t.d  6 er góður hraði
KULU_HRADI = 5  # hér þarftu að breyta hraðanum á skotunum  t.d 5 er hæfilegur hraði
FONT_NAME = pygame.font.match_font("Arial","bold")

"""


img_dir = os.path.join(game_dir, "img")

"""
# Directory containing game files
game_dir = os.path.dirname(__file__)
img_dir =  os.path.join(game_dir, "space_img")# set myndirna
snd_dir = os.path.join(game_dir, "snd")#set hljóðið

# Game init
pygame.init()
pygame.mixer.init()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("geim innrásarher")#hér þarftu setja inn titil leiksins milli gæsalappanna  t.d Pizzu innrásarher
clock = pygame.time.Clock()


def draw_text(surf, text, size, x, y):
    """Draw text on the screen"""
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    """Sprite for player"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spaceship_img, (61, 80))#bý til geimskipið og set myndina í og stærð
        #self.img = pygame.image.load("space_img/spaceship.jpg").convert()#sett inn mynd fyrir geimskipi
        self.image.set_colorkey(WHITE)#make white transparant virkar ekki
        self.rect = self.image.get_rect()
        self.radius = 31  # Hitbox radius
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.bottom = HEIGHT
        self.x_speed = LEIKMADUR_HRADI#set hraðan
        # Automatic fire (while holding FIRE button)
        self.fire_delay = 150  # Delay in ms to wait between shots
        self.last_fired = pygame.time.get_ticks()

    def update(self):
        # By default, player speed is 0
        self.x_speed = 0

        # Change speed based on user input
        keystate = pygame.key.get_pressed()
        if keystate[LEFT]:
            self.x_speed = -LEIKMADUR_HRADI#ferð til vinstri
        if keystate[RIGHT]:
            self.x_speed = LEIKMADUR_HRADI#ferð til hægri
        if keystate[FIRE]:
            self.fire()#notar spacebar til að skjóta getur haldið honum inni

        # Move player horizontally according to speed
        self.rect.x += self.x_speed

        # Constrain player within screen
        if self.rect.left < 0:
            self.rect.left = 0#getur ekki farið af skjánum
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def fire(self):
        # If fire_delay has passed since last shot, fire
        now = pygame.time.get_ticks()
        if now - self.last_fired > self.fire_delay:
            self.last_fired = now
            # Create a new bullet, add it to sprites and play fire sound
            bullet = Bullet(self.rect.centerx, self.rect.top)
            sprites.add(bullet)#sit skotinn í sprite
            bullets.add(bullet)#sit skotinn í grúpuna
            fire_sound.play()#kemur hljíoð í hvert skipti sem það er skotið


class Mob(pygame.sprite.Sprite):
    """Enemies in the game"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # bý til mynd fyrir geimverurna
        self.img = pygame.transform.scale(mob_images, (28,60)).convert()#sett inn mynd fyrir geimverur
        self.img.set_colorkey(BLACK)#make black transparant virkar ekki
        self.image = self.img.copy()  # Copy image to improve performance of rotation
        self.rect = self.img.get_rect()
        """
        self.image_orig = pygame.transform.scale(random.choice(mob_images), (28, 60))
        self.image = self.image_orig.copy()  # Copy image to improve performance of rotation
        self.rect = self.image.get_rect()
        """
        # Mobs start at random positions off screen
        self.rect.x = random.randint(0, WIDTH - self.rect.width)#er x staðsetninginn þeira
        self.rect.y = random.randint(-100, -40)#eru y staðsetninginn þeira
        # þeir eru með random hraða frá 1-8 í x og -3til 3 í y getur verið miss erfit
        self.y_speed = random.randint(1, 8)#hraði þeira lárétt
        self.x_speed = random.randint(-3, 3)#hraði þeirra lóðrétt
        # Mobs rotate at varying speeds þetta gildir ekki hér
        self.rotation = 0
        self.rotation_speed = random.randint(-8, 8)
        self.last_rotated = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        # Rotate mob every 50 ticks gildir ekki fyrir myndirnar sem ég er með
        if now - self.last_rotated > 50:
            self.last_rotated = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            #ignore
            # Create a new image based on the original using the new rotation value (degrees)
            #new_image = pygame.transform.rotate(self.image_orig, self.rotation)

            # Update rect with rotation
            old_center = self.rect.center
            # Update mob
            #and ignore
            #self.image = new_image
            #self.rect = self.image.get_rect()

            self.rect.center = old_center

    def update(self):
        self.rotate()
        # Move mobs according to speed
        self.rect.x += self.x_speed# færir geimverurnar í x átt
        self.rect.y += self.y_speed# og y átt
        # If enemy goes off the bottom or the sides, push it to the top
        if self.rect.top > HEIGHT + 10 or self.rect.left < -60 or self.rect.right > WIDTH + 60:#þer eru setir sjálfkrafa á toppin af skjánum og koma aftur ef þeir fara niður á borninn á sjánum
            self.rect.x = random.randint(0, WIDTH - self.rect.width)#er með random hraða en er ekki alveg viss hvað þetta gerir tbh
            # Mobs start at varying distances off-screen, with random vertical speeds
            self.rect.y = random.randint(-100, -40)#þetta settur geimverurnar aff skjánum þar sem þær byrja svo koma þær
            self.y_speed = random.randint(1, 8)#er með random hraða


class Bullet(pygame.sprite.Sprite):
    """Bullets shot by the player"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (15, 28)).convert()#set in mynd fyrir skotinn
        self.image.set_colorkey(WHITE)#make white transparant
        self.rect = self.image.get_rect()
        """
        self.image = pygame.transform.scale(bullet_img, (15, 28))
        self.rect = self.image.get_rect()
        """
        # x and y are the coordinates of the player, passed as arguments
        self.rect.bottom = y#set x staðsetningu myðað við leikamninn
        self.rect.centerx = x#set y staðsetningu
        self.y_speed = -KULU_HRADI#set hraða kúlunar

    def update(self):
        self.rect.y += self.y_speed#hraði kúlurnar
        # If bullet goes off screen, henni er eytt
        if self.rect.bottom < 0:
            self.kill()#henni er eytt


def show_game_over():
    """Game over screen, shown before game starts and after player dies"""
    # Stop playing music and clear screen
    screen.blit(background, background_rect)
    pygame.mixer.music.stop()
    # Draw text to screen
    # Game title
    draw_text(screen, "innrásar herinn", 64, WIDTH / 2, HEIGHT / 5)# sett inn nafn á leiknum sem kemur upp á byrjunar skjánum
    # Controls
    draw_text(screen, "Hreyfing:Örva takkar", 28, WIDTH / 2, HEIGHT * 2 / 5)# þetta kemur líka upp á byrjunar skjánum og seigir hvernig þú hreyfir karakterinn
    draw_text(screen, "Skot: Bilstöng(space) ", 28, WIDTH / 2, HEIGHT / 2)#sigir þér hvernig þú átt að skjóta
    draw_text(screen, "Hætta: Lausnarhnappur(escape)", 28, WIDTH / 2, HEIGHT * 3 / 5)#og segir þér að þú getur hætt með escape
    # Instructions to start
    draw_text(screen, "Veldu hvaða takka sem er til að byrja!", 28, WIDTH / 2, HEIGHT * 3 / 4)#og hvernig þú byrjar leikinn
    # Flip display
    pygame.display.flip()

    # Wait for user input
    waiting = True#býður eftir þér
    key_pressed = False#þannga til þetta verður True ie. þegar þú ýtir á taka

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            # If user closes the window, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
            # If user presses any key, start game
            # Key must be pressed and then released to start game
            # This prevents KEYUP events from keys that were pressed during the previous game from starting a new one
            if event.type == pygame.KEYDOWN:
                # If user presses the QUIT key, quit the game
                if event.key == QUIT:
                    pygame.quit()#ef þú ýtir á escape hættiru í leiknum
                key_pressed = True
            if event.type == pygame.KEYUP:
                if key_pressed:
                    waiting = False#takanum þarf að vera sleppt til að byrja leikinn

#ignore
#mob_list = ["mob.png", "mob1.png"]
# #ignore background = pygame.image.load(os.path.join(img_dir, "background.jpg")).convert()# hér getur þú skipt um bakgrunnsmynd nafnið

# Load all graphics
# Background
background = pygame.image.load(os.path.join(img_dir, "space.jpg"))#sett myndinna af bakgurninum
background = pygame.transform.scale(background, (WIDTH, HEIGHT))#sit scaleið af bakgruninum
background_rect = background.get_rect()#bý til rect fyrir bakgruninn
# Player spaceship
spaceship_img = pygame.image.load(os.path.join(img_dir, "spaceship.jpg")).convert_alpha()#bý til mynd fyrir spilarann virkar ekki nema með os path join
spaceship_rect = spaceship_img.get_rect()#ekki mikilvægt hélt ég þrufti þetta en var ekki viss
# aliens
mob_images = pygame.image.load(os.path.join(img_dir,"alien.png")).convert_alpha()#bý til mynd fyrir geimverurnar
mob_rect = mob_images.get_rect()#ekki mikilvægt
# Bullet
bullet_img = pygame.image.load(os.path.join(img_dir, "missile.png")).convert_alpha()#bý til mynd fyrir skotinn
bullet_rect = bullet_img.get_rect#en og aftur ekki mikilvægt

# Load all sounds

fire_sound = pygame.mixer.Sound(os.path.join(snd_dir, "fire.wav"))#bý til hljóð firir skotinn
expl_list = ["expl0.wav", "expl1.wav"]#bý til lista fyrir sprengjurnar
expl_sounds = [pygame.mixer.Sound(os.path.join(snd_dir, snd_name)) for snd_name in expl_list]#tekur úr listanum með sprengju hljóðinn og velur af random
# Background music
pygame.mixer.music.load(os.path.join(snd_dir, "background.ogg"))#virkar ekki á að vera bakkgruns hlóðið

#bý til grúpurnar virkar ekki nema þær séu hér
sprites = pygame.sprite.Group()#fyrir sprites
mobs = pygame.sprite.Group()#fyrir geimverurna
bullets = pygame.sprite.Group()#fyrir skotinn
player = Player()#bý til spilaran
sprites.add(player)#sett spilarann í sprite grúpuna
score = 0#geri scorið

# Game loop
game_over = True
running = True
while running:
    # Game over screen is shown on first run and after player dies
    if game_over:
        show_game_over()

        # When game over loop ends, start game
        game_over = False
        #work in progress pygame.mixer.music.play(loops=-1)  # Loop background music infinitely
        # When user chooses to play, initialize game
        # Create sprites
        sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        # Create 8 mobs and add them to the sprite groups
        for _ in range(8):
            m = Mob()
            sprites.add(m)
            mobs.add(m)
        # Create bullet sprite group
        bullets = pygame.sprite.Group()
        # Add player to sprite group
        player = Player()
        sprites.add(player)

        # Initial score is 0
        score = 0

    # Game
    # Run game loop at specified speed æ´ v
    clock.tick(FPS)
    # Process events
    for event in pygame.event.get():
        # Stop running game if user quits
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # End game (go to game over) if user hits the QUIT key
            if event.key == QUIT:
                game_over = True#þegar þú tapar

    # Update
    sprites.update()

    # Check for bullet collisions with mobs
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)  # Kill both mob and bullet if they collide
    # If a mob is killed, add to score and spawn a new mob
    for hit in hits:# í hvert skipti sem þú hitir óvinina færðu eitt stig
        score += 1  # 1 kill = 1 pt
        m = Mob()#bý til geimverur
        sprites.add(m)# sit mobana í sprite
        mobs.add(m)#sit mobana í grúpuna
        random.choice(expl_sounds).play()  # Play one of the explosion sounds

    # Check for mob collisions with player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    # If player is hit by mob, player dies and game ends
    if hits:
        game_over = True#ert dauður

    # Render
    screen.blit(background, background_rect)#bakgrunurinn
    #screen.blit(spaceship_img, spaceship_rect)

    sprites.draw(screen)
    # Draw score on top
    draw_text(screen, str(score), 24, WIDTH / 2, 10)#set scorið á toppinn
    # Flip display
    pygame.display.flip()

# When loop ends, quit game
pygame.quit()


'''


pygame.init()
pygame.mixer.init()

width = 600
height = 600
fps = 60

#litir
black=(0,0,0)
blue=(0,0, 255)
green=(0,128,0)
red=(255,0,0)
white=(255,255,255)
yellow=(255,255,0)

left = pygame.K_LEFT
right = pygame.K_RIGHT
fire = pygame.K_SPACE
quite = pygame.K_ESCAPE


spilari_hradi = 6 #hraði leikmans
skot_speed = 5 #hraði skots

screen = pygame.display.set_mode((width, height))

"""
#directory sem hedlur leikja filum
game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "img")
snd_dir = os.path.join(game_dir, "sound")
"""

#font_name = pygame.font.match_font_match("Arial","bold")
font_name = pygame.font.match_font("Arial","bold")
BLOCKERS_POSITION = 450 #kannski kanski ekki
ENEMY_DEFAULT_POSITION = 65  # Initial value for a new game
ENEMY_MOVE_DOWN = 35


"""
class Veggur(object):#geri veggina
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
"""#ekki mikilvægt


class Geimskip(pygame.sprite.Sprite):# geri geimskip
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("space_img/spaceship.jpg").convert()#sett inn mynd fyrir geimskipi
        self.img.set_colorkey(white)#make white transparant
        self.rect = self.img.get_rect()
        self.radius = 31 #hitboxinn
        self.rect.center = (width / 2, height / 2)
        self.rect.bottom = height
        self.x_speed = spilari_hradi
        #heldur inn skot takanum í stað þesss að ýta
        self.fire_delay = 150
        self.last_fired = pygame.time.get_ticks()

    def move(self):
        #default hraði er 0
        self.xspeed = 0

        #hreyfingar input hjá spilara
        keystate = pygame.key.get_pressed()
        if keystate[left]:
            self.x_speed = -spilari_hradi
        if keystate[right]:
            self.x_speed = spilari_hradi
        if keystate[fire]:
            self.fire()
        #hreyfing horizontally með hraða
        self.rect.x += self.x_speed
        #heldur spilaranum í skjánum
        if self.rect.left < 0:
            self.rect.left =0
        if self.rect.right > width:
            self.rect.right = width
    def fire(self):
        #ef skot delay er buinn síðan þú skaust síðast
        now = pygame.time.get_ticks()
        if now - self.last_fire > self.fire_delay:
            self.last_fire = now
            #býr til ný skot setur það í sprites og spilar hlljóð
            skot = Missile(self.rect.centerx, self.rect.top)
            sprite.add(skot)
            skot.add(skot)
            fire_sound.play()#work in progress

        """
        self.speedx = 0
        if event.type == KEYDOWN and event.key == k_LEFT:
            self.speedx = -1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.speedx = 1
            """
    def skot(self):

        """
        missile = Missile(self.rect.centerx,self.rect.top)
        allSprites.add(missile)
        Missile.add(missile)
        """
class Geimverur(pygame.sprite.Sprite):#óvinirnir
    def __init__(self,row,column):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("space_img/alien.png").convert()#sett inn mynd fyrir geimverur
        self.img.set_colorkey(white)#make white transparant
        self.rect = self.img.get_rect()
        self.row = row
        self.column = column
        """
        #random staðsetning hjá óvini af skjánum
        self.rect.x = random.randint(0,width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        """
class geimverugroup(pygame.sprite.Group):#geri fyrir hóp af óvinum sem eru settir inn
    def __init__(self, column, row):
        pygame.sprite.Group.__init__(self)
        self.enemies = [[None] * column for _ in range(row)]
        self.columns = column
        self.rows = row
        self.leftAddMove = 0
        self.rightAddMove = 0
        self.moveTime = 600
        self.direction = 1
        self.rightMoves = 30
        self.leftMoves = 30
        self.moveNumber = 15
        self.timer = pygame.time.get_ticks()
        self.bottom = pygame.enemyPosition + ((row - 1) * 45) + 35
        self._aliveColumns = list(range(column))
        self._leftAliveColumn = 0
        self._rightAliveColumn = column - 1

    def update(self, current_time):
        if current_time - self.timer > self.moveTime:#hverning óvininrir hreyfa sig frá hægri til vinstri
            if self.direction == 1:
                max_move = self.rightMoves + self.rightAddMove
            else:
                max_move = self.leftMoves + self.leftAddMove

            if self.moveNumber >= max_move:
                self.leftMoves = 30 + self.rightAddMove
                self.rightMoves = 30 + self.leftAddMove
                self.direction *= -1
                self.moveNumber = 0
                self.bottom = 0
                for enemy in self:
                    enemy.rect.y += ENEMY_MOVE_DOWN
                    enemy.toggle_image()
                    if self.bottom < enemy.rect.y + 35:
                        self.bottom = enemy.rect.y + 35
            else:
                velocity = 10 if self.direction == 1 else -10
                for enemy in self:
                    enemy.rect.x += velocity
                    enemy.toggle_image()
                self.moveNumber += 1

            self.timer += self.moveTime

class Missile(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(bullet_img, (15,28)) ignore
        self.img = pygame.image.load("space_img/missile.png").convert()#set in mynd fyrir skotinn
        self.img.set_colorkey(white)#make white transparant
        self.rect = self.img.get_rect()
        #self.rect = self.image.get_rect("space_img/missile.png") ignore
        #set in x og y ferðir spilarans sem arguments
        self.rect.bottom = y
        self.rect.centers = x
        self.y_speed = skot_speed


pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((640, 480))

#veggir = list()#geri lista fyrir veggi
geimskip = Geimskip()#geri spilaran
geimverur = Geimverur(12,3)#geri óvinina
x = 0
y=0
running = True

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        geimskip.move(-2,0)
    if key[pygame.K_RIGHT]:
        geimskip.move(2,0)
'''
