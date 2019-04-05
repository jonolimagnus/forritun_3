import pygame

# This demo is based in most parts on a collision demo at the original PyGqme website.
# http://www.pygame.org/project-Rect+Collision+Response-1061-.html
# accessed on 12-10-2016
# Information about the original author not found(broken link ?)

# In this demo we now have shields that disappear when they collide with the player.
# This is done by removing the respective shield from the list of shields.
# The code-segments needed for this are in lines no:
# 49 - 52
# 68 - 70
# 81
# 114 - 115
# 155 - 156
# Also note that an S has been added to the map to place the shields.


# Class for the Player(the orange dude)
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Move the rectangle
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall
        for a_brick in bricks:
            if self.rect.colliderect(a_brick.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = a_brick.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = a_brick.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = a_brick.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = a_brick.rect.bottom

        # If you collide with a shield(green stuff)
        for a_shield in shields:
            if self.rect.colliderect(a_shield.rect):
                print("Got myself a Shield")
                shields.remove(a_shield)


#  A class to hold a wall rectangle
class Brick(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# A class to hold the magic rectangle
class MagicBox(object):
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# A class to hold the shields the player can pick up
class Shield(object):
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialize
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
bricks = list()     # List to hold the walls
shields = list()    # List to hold the shields
player = Player()   # Create the player

# Holds the level layout in a list of strings.
maze = [
"WWWWWWWWWWWWWWWWWWWW",
"W           S      W",
"W         WWWWWW   W",
"W   WWWWS      W   W",
"W   W        WWWW  W",
"W WWW  WWWW     M  W",
"W   W     W W      W",
"W   W    SW   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W   S  WW     S  W",
"W W   WWWW   WWW   W",
"W     SW   E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

# Parse the maze string above. W = wall, E = exit, M = magic box
x = 0
y = 0
for row in maze:
    for col in row:
        if col == "W":
            bricks.append(Brick((x, y)))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        if col == "M":
            magic_rect = MagicBox((x,y))
        if col == "S":
            shields.append(Shield((x,y)))
        x += 16
    y += 16
    x = 0

running = True

while running:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Check to see if the player has collided the magic box or the exit.
    if player.rect.colliderect(end_rect):
        print("You win!")
        raise SystemExit()
        #raise (SystemExit, 'You win!')
    if player.rect.colliderect(magic_rect):
        print("You lose!")
        raise SystemExit()
        #raise (SystemExit(), 'You lose!')

    # Draw the scene
    screen.fill((0, 0, 0))
    # every brick in the walls is drawn
    for brick in bricks:
        pygame.draw.rect(screen, (255, 255, 255), brick.rect)

    # every shield is drawn
    for shield in shields:
        pygame.draw.rect(screen, (0, 255, 20), shield.rect)

    # the others are drawn
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (0, 0, 255), magic_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)

    pygame.display.flip()
