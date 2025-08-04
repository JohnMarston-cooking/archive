import pygame
import sys

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joystick Control")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)
DARK_GREY = (60, 60, 60)

square_size = 50
x = (width - square_size) // 2
y = height - square_size
velocity_y = 0
gravity = 0.5
jump_strength = -10
on_ground = True
speed = 5

button_width = 100
button_height = 40
button_x = (width - button_width) // 2
button_y = 20
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

joystick_bar_width = 120
joystick_bar_height = 10
joystick_bar_x = (width - joystick_bar_width) // 2
joystick_bar_y = button_y + button_height + 20

joystick_knob_radius = 12
joystick_knob_x = joystick_bar_x + joystick_bar_width // 2
joystick_dragging = False

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and on_ground:
                velocity_y = jump_strength
                on_ground = False
            
            elif pygame.Rect(joystick_knob_x - joystick_knob_radius, joystick_bar_y - joystick_knob_radius,
                             joystick_knob_radius * 2, joystick_knob_radius * 2).collidepoint(event.pos):
                joystick_dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            joystick_dragging = False
            joystick_knob_x = joystick_bar_x + joystick_bar_width // 2  

        elif event.type == pygame.MOUSEMOTION and joystick_dragging:
            mx = event.pos[0]
            
            joystick_knob_x = max(joystick_bar_x, min(mx, joystick_bar_x + joystick_bar_width))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_strength
        on_ground = False
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed

    
    mid_x = joystick_bar_x + joystick_bar_width // 2
    offset = joystick_knob_x - mid_x
    x += (offset / (joystick_bar_width // 2)) * speed  

    
    velocity_y += gravity
    y += velocity_y

    
    if y >= height - square_size:
        y = height - square_size
        velocity_y = 0
        on_ground = True

    
    x = max(0, min(x, width - square_size))

    
    pygame.draw.rect(screen, RED, button_rect)

    
    pygame.draw.rect(screen, GREY, (joystick_bar_x, joystick_bar_y, joystick_bar_width, joystick_bar_height))
    
    pygame.draw.circle(screen, DARK_GREY, (joystick_knob_x, joystick_bar_y + joystick_bar_height // 2), joystick_knob_radius)

    
    pygame.draw.rect(screen, WHITE, (x, y, square_size, square_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
