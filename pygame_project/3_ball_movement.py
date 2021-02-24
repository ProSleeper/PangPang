import os
import pygame
import time
import copy


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

    def GetRectSize(self):
        return self.size;

def IntersectCircleAndSquare(circleX, circleY, circleR, squareX, squareY, squareW, squareH):

    """
    1. 원의 x,y 좌표 중 하나라도 사각형의 영역 안에 포함되는 지 판별
        1-1. 사각형의 크기를 상하좌우 각각 원의 반지름 만큼 늘리고
        1-2. 해당 영역에 원의 중심점이 포함되는지 검사 -> 포함 된다면 충돌
    2. 사각형의 원래 크기일때의 꼭지점 4개가 원의 영역에 포함되는지 검사 -> 포함 된다면 충돌
    """


    circleXpos      = circleX;
    circleYpos      = circleY;
    circleRadius    = circleR;

    squareXpos      = squareX;
    squareYpos      = squareY;
    squareWitdh     = squareW;
    squareHeight    = squareH;

    if squareXpos <= circleXpos <= squareWitdh or squareYpos <= circleYpos <= squareHeight:
        if squareXpos - circleRadius  <= circleXpos <= squareWitdh + circleRadius and \
            squareYpos - circleRadius  <= circleYpos <= squareHeight + circleRadius:
            return True; # 충돌
    elif IntersectDotAndCircle(squareXpos, squareYpos, circleXpos, circleYpos, circleRadius) or IntersectDotAndCircle(squareXpos, squareHeight, circleXpos, circleYpos, circleRadius) or \
        IntersectDotAndCircle(squareWitdh, squareYpos, circleXpos, circleYpos, circleRadius) or IntersectDotAndCircle(squareWitdh ,squareHeight, circleXpos, circleYpos, circleRadius):
        return True;

            
    return False;
    
def IntersectDotAndCircle(dotX, dotY, circleX, circleY, circleR):
    dotXpos         = dotX;
    dotYpos         = dotY;
    
    circleXpos      = circleX;
    circleYpos      = circleY;
    circleRadius    = circleR;
    
    dotToCircleDistance = 0;

    dotToCircleDistance = ((dotXpos - circleXpos) * (dotXpos - circleXpos)) + ((dotYpos - circleYpos) * (dotYpos - circleYpos));

    if dotToCircleDistance <= (circleRadius * circleRadius):
        return True;
        
    return False;

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
character_to_y  = 0;
character_speed = 5;

weapon = GameObject(os.path.join(image_path, "weapon.png"));
weapons  = list();
weapon_speed = 10;

ball_images = [ GameObject(os.path.join(image_path, "poong.png")), 
                GameObject(os.path.join(image_path, "balloon2.png")), 
                GameObject(os.path.join(image_path, "balloon3.png")), 
                GameObject(os.path.join(image_path, "balloon4.png"))]

#공이 떨어지는 속도
#이건 작성자가 임의로 테스트 해보고 정한듯
ball_speed_y = [-18, -15, -12, -9];

balls = list();
ballsInitValue = list();
#공의 초기 값
balls.append({"pos_x" : 50,"pos_y" : 50, "img_idx" : 0, "to_x" : 3, "to_y" : -6, "init_spd_y" : ball_speed_y[0]});
ballsInitValue.append({"pos_x" : 50,"pos_y" : 50, "img_idx" : 0, "to_x" : 3, "to_y" : -6, "init_spd_y" : ball_speed_y[0]});

running = True;
drawing = True;

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
            elif event.key == pygame.K_UP:
                character_to_y -= character_speed;
            elif event.key == pygame.K_DOWN:
                character_to_y += character_speed;
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character.GetPositionX() + (character.GetWidth() / 2) - (weapon.GetWidth() / 2);
                weapon_y_pos = character.GetPositionY();
                weapons.append([weapon_x_pos, weapon_y_pos]);
            elif event.key == pygame.K_RETURN:
                drawing = True;
                balls = copy.deepcopy(ballsInitValue);
                character.SetPosition((SCREEN_WIDTH / 2) - (character.GetWidth() / 2), SCREEN_HEIGHT - character.GetHeight() - stage.GetHeight())

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0;
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0;

    if drawing:

        character.SetPositionX(character.GetPositionX() + character_to_x);
        character.SetPositionY(character.GetPositionY() + character_to_y);
                    
        if character.GetPositionX() < 0:
            character.SetPositionX(0);
        elif character.GetPositionX() > SCREEN_WIDTH - character.GetWidth():
            character.SetPositionX(SCREEN_WIDTH - character.GetWidth());
            
        weapons = [[w[0], w[1] - weapon_speed] for w in weapons];
        weapons = [[w[0], w[1]] for w in weapons if w[1] > 0];


        #enumerate는 반복문 사용시 몇번째인지 확인하려고 씀
        #인덱스와 원소값을 tuple형태로 반환 해줌 예) (0, 5), (1, 12)
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"];
            ball_pos_y = ball_val["pos_y"];
            ball_img_idx = ball_val["img_idx"];

            ball_size = ball_images[ball_img_idx].GetRectSize();
            ball_width = ball_size[0];
            ball_height = ball_size[1];

            if ball_pos_x < 0 or ball_pos_x > SCREEN_WIDTH - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1;

            if ball_pos_y >= SCREEN_HEIGHT - stage.GetHeight() - ball_height:
                ball_val["to_y"] = ball_val["init_spd_y"]
            else:
                ball_val["to_y"] += 0.5;

            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]
            
        
        screen.blit(background.GetObject(), background.GetPosition())

        for weapon_x_pos, weapon_y_pos in weapons:
            weapon.SetPosition(weapon_x_pos, weapon_y_pos)
            if IntersectCircleAndSquare((ball_pos_x + (ball_images[ball_img_idx].GetWidth() / 2)), (ball_pos_y + (ball_images[ball_img_idx].GetWidth() / 2)), (ball_images[ball_img_idx].GetWidth() / 2), weapon.GetPositionX(), weapon.GetPositionY(), (weapon.GetPositionX() + weapon.GetWidth()), (weapon.GetPositionY() + weapon.GetHeight())):
                weapons.remove([weapon.GetPositionX(), weapon.GetPositionY()])
                balls[0]["img_idx"] = 1;
                
            screen.blit(weapon.GetObject(), weapon.GetPosition())

        for idx, val in enumerate(balls):
            ball_pos_x = val["pos_x"]
            ball_pos_y = val["pos_y"]
            ball_img_idx = val["img_idx"]
            ball_images[ball_img_idx].SetPosition(ball_pos_x, ball_pos_y)
            #print(character.GetHeight())
            #충돌판정 원과 사각의 충돌 제대로 됨
            if IntersectCircleAndSquare((ball_pos_x + (ball_images[ball_img_idx].GetWidth() / 2)), (ball_pos_y + (ball_images[ball_img_idx].GetWidth() / 2)), (ball_images[ball_img_idx].GetWidth() / 2), character.GetPositionX(), character.GetPositionY(), (character.GetPositionX() + character.GetWidth()), (character.GetPositionY() + character.GetHeight())):
                print("충돌");
                drawing = False;
                
            else:
                print("안충돌")
            screen.blit(ball_images[ball_img_idx].GetObject(), ball_images[ball_img_idx].GetPosition());

        # 이 blit이라는 메서드는 객체를 생성해준다기보다 source에 해당하는 이미지를 복사해준다는 개념인듯
        screen.blit(stage.GetObject(), stage.GetPosition())
        screen.blit(character.GetObject(), character.GetPosition())

    pygame.display.update();



pygame.quit();
