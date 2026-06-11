import time
import random
import pygame
pygame.init()

COLOR = (255, 255, 255) #white
COLOR1 = (0, 0, 0)  #black
COLOR2 = (255, 0, 0) #red
COLOR3 = (0, 255, 0) #green
COLOR4 = (0, 0, 255) #blue


box_len=900
box_height=600

add_caption=pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("Snake Game")

TIMER=pygame.time.Clock()

snake_block=18
snake_speed = 10

display_style=pygame.font.SysFont("comicsansms", 35, bold=True)
score_style=pygame.font.SysFont("comicsansms", 25, bold=True)

def final_score(score):
    value=score_style.render("Your Score: "+str(score), True, COLOR2)
    add_caption.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(add_caption, COLOR3, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    mesg=display_style.render(msg, True, color)
    add_caption.blit(mesg, [box_len/6, box_height/3])

def game_start():
    game_over=False
    game_close=False

    x1=box_len/2
    y1=box_height/2

    x1_change=0;
    y1_change=0;

    snake_List=[]
    Length_of_snake=1

    foodx_pos=random.randrange(0, box_len-snake_block, snake_block)
    foody_pos=random.randrange(0, box_height-snake_block, snake_block)  

    while not game_over:

        while game_close==True:
            add_caption.fill(COLOR1)
            display_message("You Lost! Press C-Play Again or Q-Quit", COLOR2)
            final_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        game_start()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0

        if x1>=box_len or x1<0 or y1>=box_height or y1<0:
            game_close=True

        x1+=x1_change
        y1+=y1_change   

        add_caption.fill(COLOR1)
        pygame.draw.rect(add_caption, COLOR2, [foodx_pos, foody_pos, snake_block, snake_block]) 
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close=True

        our_snake(snake_block, snake_List)
        final_score(Length_of_snake - 1)    
        pygame.display.update()
        if x1==foodx_pos and y1==foody_pos:
            foodx_pos=random.randrange(0, box_len-snake_block, snake_block)
            foody_pos=random.randrange(0, box_height-snake_block, snake_block)  
            Length_of_snake+=1

        TIMER.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_start()