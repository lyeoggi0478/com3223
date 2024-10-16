import pygame

D_SIZE = (800, 600)

pygame.init();

RED = (255, 0, 0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);
WHITE = (255, 255, 255);

#snake
snake_size = 10;
snake_pos_x = D_SIZE[0]/2 - snake_size/2;
snake_pos_y = D_SIZE[1]/2 - snake_size/2;
snake_pos_x_change = 0;
snake_pos_y_change = 0;



screen = pygame.display.set_mode(D_SIZE);
screen = pygame.display.set_caption("snake gmae");
pygame.display.update();


running = True;

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False;
        if event.type == pygame.K_UP :
            snake_pos_x_change = 0
            snake_pos_y_change = -10
        elif event.type == pygame.K_DOWN :
            snake_pos_x_change = 0
            snake_pos_y_change = 10
        elif event.type == pygame.K_LEFT :
            snake_pos_x_change = -10
            snake_pos_y_change = 0
        elif event.type == pygame.K_RIGHT :
            snake_pos_x_change = 10
            snake_pos_y_change = 0
            
        snake_pos_x += snake_pos_x_change
        snake_pos_y += snake_pos_y_change
        

    loc = [snake_pos_x, snake_pos_y, snake_size, snake_size];
    pygame.draw.rect(screen, RED, loc);
    

pygame.quit();
