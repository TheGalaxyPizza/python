import pygame
import math
import constants

class Character:
    def __init__(self, x, y, health, mob_animations, char_type):
        self.char_type = char_type
        self.flip = False
        self.animation_list = mob_animations[char_type]
        self.frame_index = 0
        self.action = 0#0 means idle, #1 means run
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.health = health
        self.alive = True

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):

        #Running
        self.running = False
        if dx != 0 or dy != 0:
            self.running = True

        #Check Character Dynamics
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

            #control diagonal speed
            if dx != 0 and dy !=0:
                dx = dx * (math.sqrt(2)/2)
                dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy


    def update(self):

        #check if character has died
        if self.health <= 0:
            self.health = 0
            self.alive = False

        #check what action the player is performing
        if self.running:
            self.update_action(1)
        else:
            self.update_action(0)

        #player animation cooldown
        animation_cooldown = 70
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):

        #check if the new action is different to the previous one.
        if new_action != self.action:
            self.action = new_action

        #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()



    def draw(self, surface):

        #Character Dynamics
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        if self.char_type == 0:
            surface.blit(flipped_image, (self.rect.x, self.rect.y - constants.SCALE * constants.OFFSET))
        else:
            surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)