import pygame
#player class
class Player():


    def __init__(self, x, y, colour, speed, health, slot, inventory):
        self.player_down = pygame.image.load('assets/player/player_dir-down.png')
        self.player_up = pygame.image.load('assets/player/player_dir-up.png')
        self.player_left = pygame.image.load('assets/player/player_dir-left.png')
        self.player_right = pygame.image.load('assets/player/player_dir-right.png')
        self.items = inventory
        #self.pain
        self.cur_item = self.items[0]
        self.slot = slot
        self.hp = health
        self.speed = speed
        self.width = 44
        self.height = 120
        self.colour = colour
        self.direction = 0 # down = 0, up = 1, left = 2, right = 3
        self.image = pygame.transform.scale(self.player_down, (64, 128))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def inv(self):
        if self.slot:
            if self.slot == 0:
                self.cur_item = 0
            if self.slot == 1:
                self.cur_item = 1
            if self.slot == 2:
                self.cur_item = 2
            if self.slot == 3:
                self.cur_item = 3
            if self.slot == 4:
                self.cur_item = 4
    
                

    def damage(self, damage):
        self.health -= damage

    def health(self):
        if self.hp == 0:
            pass

    def move(self):
        #get them clicci keys
        key = pygame.key.get_pressed() # down = 0, up = 1, left = 2, right = 3
        if key:
            if key[pygame.K_a]:
                self.rect.x -= self.speed
                self.direction = 4 # left
            if key[pygame.K_d]:
                self.rect.x += self.speed
                self.direction = 3 # right
            if key[pygame.K_w]:
                self.rect.y -= self.speed
                self.direction = 2 # up
            if key[pygame.K_s]:
                self.rect.y += self.speed
                self.direction = 1 # down   

    def draw(self, screen):

        if self.direction:
            if self.direction == 1:
                self.image = pygame.transform.scale(self.player_down, (64, 128))
            if self.direction == 2:
                self.image = pygame.transform.scale(self.player_up, (64, 128))
            if self.direction == 4:
                self.image = pygame.transform.scale(self.player_left, (64, 128))
            if self.direction == 3:
                self.image = pygame.transform.scale(self.player_right, (64, 128))
        screen.blit(self.image, (self.rect.x -10, self.rect.y -5))
        pygame.draw.rect(screen,self.colour, self.rect, 2)
