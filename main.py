import pygame

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h) 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)

fish_image = pygame.image.load('fish.png')
fish_image = pygame.transform.smoothscale(fish_image, (80, 80))
fish_rect = fish_image.get_rect()

def main():
  while True: 
    clock.tick(60)
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()   


