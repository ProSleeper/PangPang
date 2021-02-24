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


running = True;
while running:
    dt = clock.tick(30);

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        


    screen.blit(background.GetObject(), background.GetPosition())
    screen.blit(stage.GetObject(), stage.GetPosition())
    screen.blit(character.GetObject(), character.GetPosition())

    pygame.display.update();



pygame.quit();
