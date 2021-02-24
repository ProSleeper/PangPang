import pygame

#내가 만든 코드
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

background = pygame.image.load("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\background.png")

character = pygame.image.load("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\character.png")
character_size = character.get_rect().size;
character_width = character_size[0];
character_height = character_size[1];

character_x_pos = (screen_width / 2) - (character_width / 2);
character_y_pos = screen_height - character_height;


to_x = 0;
to_y = 0;

character_speed = 0.6;

enemy = pygame.image.load("C:\\Users\\ingn\\Documents\\python\\PangPang\\pygame_basic\\enemy.png")
enemy_size = character.get_rect().size;
enemy_width = enemy_size[0];
enemy_height = enemy_size[1];

enemy_x_pos = (screen_width / 2) - (enemy_width / 2);
enemy_y_pos = (screen_height / 2) - (enemy_height / 2);

game_font = pygame.font.Font(None, 40);

total_time = 10;

start_ticks = pygame.time.get_ticks();
print(start_ticks);

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
            elif event.key == pygame.K_UP:
                to_y -= character_speed;
            elif event.key == pygame.K_DOWN:
                to_y += character_speed;
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0;
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0;
                    
    character_x_pos += to_x * dt;
    character_y_pos += to_y * dt;        
    
    if 0 > character_x_pos:
        character_x_pos = 0;
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width;

    if 0 > character_y_pos:
        character_y_pos = 0;
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height;
        

    character_rect = character.get_rect();
    character_rect.left = character_x_pos;
    character_rect.top = character_y_pos;

    enemy_rect = enemy.get_rect();
    enemy_rect.left = enemy_x_pos;
    enemy_rect.top = enemy_y_pos;
    


    bCol = IntersectRect(character_rect, enemy_rect);

    if IntersectRect(character_rect, enemy_rect):
        print("충돌했습니다.");
        running = False;
        
    screen.blit(background, (0,0));
    screen.blit(character, (character_x_pos, character_y_pos));
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos));

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 ;

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255));
    screen.blit(timer, (10, 10));

    if total_time - elapsed_time <= 0:
        print("타임 아웃");
        running = False;
        

    pygame.display.update();

pygame.time.delay(2000);
pygame.quit();

