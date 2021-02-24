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

running = True;
while running:
    dt = clock.tick(60);    # 이 clock.tick 을 써서 프레임을 만듬 값이 60이면 1초를 60나눈 값인 0.016초마다 멈춰서 실행이 됨


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        
    pygame.display.update();

pygame.quit();

