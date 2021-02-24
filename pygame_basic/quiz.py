import pygame
import random


class QuizObject():
    def __init__(self, filePath):
        self.object = pygame.image.load(filePath);
        self.size   = self.object.get_rect().size;
        self.width  = self.size[0];
        self.height = self.size[1];

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

        

#내가 만든 코드 사각형 충돌 판정
def IntersectRect(rect1, rect2):
    #rect로 넘겨져 오는 값 (x, y, width, height)
    if rect1.left <= rect2.right and rect1.right >= rect2.left and rect1.top <= rect2.bottom and rect1.bottom >= rect2.top:
        return True;
    else:
        return False;


        
pygame.init();


screen_width    =   480;
screen_height   =   640;
screen = pygame.display.set_mode((screen_width, screen_height));

pygame.display.set_caption("PangPang");
clock = pygame.time.Clock();

background = pygame.image.load("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\background.jpg")
enemy = pygame.image.load("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\enemy.png")


character = QuizObject("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\character.png");
character.SetPosition((screen_width / 2) - (character.width / 2), screen_height - character.height);

enemy = QuizObject("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\enemy.png");
enemy.SetPosition(random.randrange(0, screen_width - enemy.width + 1), -enemy.height);

to_x = 0;

character_speed = 0.6;
enemySpeed = 0.5;

running = True;
while running:
    dt = clock.tick(60);    # 이 clock.tick 을 써서 프레임을 만듬 값이 60이면 1초를 60나눈 값인 0.016초마다 멈춰서 실행이 됨


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed;
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed;

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0;
            
    character.SetPositionX(character.xPos + (to_x * dt));
    enemy.SetPositionY(enemy.yPos + (enemySpeed * dt));

    if 0 > character.GetPositionX():
        character.SetPositionX(0);
    elif character.GetPositionX() > screen_width - character.width :
        character.SetPositionX(screen_width - character.width);

    character_rect = character.object.get_rect()
    character_rect.left = character.GetPositionX();
    character_rect.top = character.GetPositionY();

    enemy_rect = enemy.object.get_rect()
    enemy_rect.left = enemy.GetPositionX();
    enemy_rect.top = enemy.GetPositionY();


    if IntersectRect(character_rect, enemy_rect):
        print("충돌")
        running = False;


    if enemy.GetPosition()[1] > screen_height:
        enemy.SetPosition(random.randrange(0, screen_width - enemy.width + 1), -enemy.height)
        
        

    screen.blit(background, (0, 0));
    screen.blit(character.object, (character.GetPosition()));
    screen.blit(enemy.object, (enemy.GetPosition()));

    pygame.display.update();

pygame.quit();

