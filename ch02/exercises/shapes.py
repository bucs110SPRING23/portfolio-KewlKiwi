import pygame

pygame.init()

screen = pygame.display.set_mode()

screen.fill("lightblue")
screen_size = screen.get_size()

dimensions1 = [0, screen_size[1] - 100, screen_size[0], 1000]
dimensions2 = [0, screen_size[1] - 96, screen_size[0], 1000]
dimensions4 = [screen_size[0]/2 + 5, (screen_size[1]/2) - 45, 70, 20]
dimensions3 = [screen_size[0]/2, (screen_size[1]/2) - 50, 80, 30]


pygame.draw.rect(screen, "black", dimensions1)
pygame.draw.rect(screen, "white", dimensions2)

pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2) + 325], 205)
pygame.draw.circle(screen, "white", [screen_size[0]/2, (screen_size[1]/2) + 325], 200)
pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2) + 125], 155)
pygame.draw.circle(screen, "white", [screen_size[0]/2, (screen_size[1]/2) + 125], 150)
pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2) - 50], 105)
pygame.draw.circle(screen, "white", [screen_size[0]/2, (screen_size[1]/2) - 50], 100)
pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2) + 325], 10)
pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2 + 50) + 125], 10)
pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2 - 25) + 125], 10)
pygame.draw.circle(screen, "black", [screen_size[0]/2 - 25, (screen_size[1]/2 - 20) - 50], 10)
pygame.draw.circle(screen, "black", [screen_size[0]/2 + 25, (screen_size[1]/2 - 20) - 50], 10)
pygame.draw.rect(screen, "black", dimensions3)
pygame.draw.rect(screen, "orange", dimensions4)

pygame.display.flip()
pygame.time.wait(2000)
