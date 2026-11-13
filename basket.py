import pygame
import random

pygame.init()
screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Catch the Blocks")
clock = pygame.time.Clock()

running = True

basket = pygame.Rect(200, 330, 80, 16)
block = pygame.Rect(220, 0, 20, 20)

font = pygame.font.Font(None, 32)
score = 0
lives = 3
paused = False
SPEED_UP = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED_UP, 10000)
fall_speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_r and (lives == 0 or score == 10):
                score = 0
                lives = 3
                basket.x = 200
                block.y = -20
                block.x = random.randint(0, 460)
                fall_speed = 3
        elif event.type == SPEED_UP:
         fall_speed += 1 

    
    if lives > 0 and score < 10 and not paused:
        keys = pygame.key.get_pressed()
        speed = 8
        
        if keys[pygame.K_LEFT]:
            basket.x -= speed
        if keys[pygame.K_RIGHT]:
            basket.x += speed
        
            
        basket.clamp_ip(screen.get_rect())

        block.y += fall_speed
        
        if block.top > 360:
            block.y = -20
            block.x = random.randint(0, 460)
            lives -= 1

        if block.colliderect(basket):
            block.y = -20
            block.x = random.randint(0, 460)
            score += 1


        screen.fill((30, 30, 46))

        pygame.draw.rect(screen, (80, 160, 255), basket)
        pygame.draw.rect(screen, (235, 80, 80), block)

        score_text = font.render(f"Score: {score}", True, (240, 240, 240))
        screen.blit(score_text, (10, 10))

        score_text = font.render(f"Lives: {lives}", True, (240, 240, 240))
        screen.blit(score_text, (370, 10))
    
    if lives == 0:
        message = font.render("Game over", True, (240, 240, 240))
        screen.blit(message, message.get_rect(center=(240, 160)))
    elif score == 10:
        message = font.render("You win!", True, (240, 240, 240))
        screen.blit(message, message.get_rect(center=(240, 160)))
    elif paused:
        message = font.render("Paused", True, (240, 240, 240))
        screen.blit(message, message.get_rect(center=(240, 160)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()