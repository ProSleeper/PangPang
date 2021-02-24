import os
import pygame


class GameObject():
    def __init__(self, filePath):
        self.object = pygame.image.load(filePath);
        self.size   = self.object.get_rect().size;
        self.width  = self.size[0];
        self.height = self.size[1];
        self.xPos   = 0;
        self.yPos   = 0;

    def GetObject(self):
        return self.object;

    def SetPosition(self, xPos, yPos):
        self.xPos   = xPos;
        self.yPos   = yPos;

    def SetPositionX(self, xPos):
        self.xPos   = xPos;

    def SetPositionY(self, yPos):
        self.yPos   = yPos;

    def GetPosition(self):
        return self.xPos, self.yPos;

    def GetPositionX(self):
        return self.xPos;

    def GetPositionY(self):
        return self.yPos;

    def GetWidth(self):
        return self.width;

    def GetHeight(self):
        return self.height;

pygame.init();

SCREEN_WIDTH    = 640;
SCREEN_HEIGHT   = 480;

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
pygame.display.set_caption("PangPang");


clock = pygame.time.Clock();

current_path = os.path.dirname(__file__);
image_path = os.path.join(current_path, "images");

background = GameObject(os.path.join(image_path, "background.png"));

stage = GameObject(os.path.join(image_path, "stage.png"));
stage.SetPosition(0, SCREEN_HEIGHT - stage.GetHeight())

character = GameObject(os.path.join(image_path, "character.png"));
character.SetPosition((SCREEN_WIDTH / 2) - (character.GetWidth() / 2), SCREEN_HEIGHT - character.GetHeight() - stage.GetHeight())

character_to_x  = 0;
character_speed = 5;

weapon = GameObject(os.path.join(image_path, "weapon.png"));
weapons  = list();
weapon_speed = 10;


running = True;
while running:
    dt = clock.tick(30);

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed;
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed;
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character.GetPositionX() + (character.GetWidth() / 2) - (weapon.GetWidth() / 2);
                weapon_y_pos = character.GetPositionY();
                weapons.append([weapon_x_pos, weapon_y_pos]);
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0;

    character.SetPositionX(character.GetPositionX() + character_to_x);
                
    if character.GetPositionX() < 0:
        character.SetPositionX(0);
    elif character.GetPositionX() > SCREEN_WIDTH - character.GetWidth():
        character.SetPositionX(SCREEN_WIDTH - character.GetWidth());
        
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons];
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0];

    screen.blit(background.GetObject(), background.GetPosition())

    for weapon_x_pos, weapon_y_pos in weapons:
        weapon.SetPosition(weapon_x_pos, weapon_y_pos)
        screen.blit(weapon.GetObject(), weapon.GetPosition())

    screen.blit(stage.GetObject(), stage.GetPosition())
    screen.blit(character.GetObject(), character.GetPosition())

    pygame.display.update();



pygame.quit();
