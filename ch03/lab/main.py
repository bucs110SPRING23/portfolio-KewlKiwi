import pygame
import random
import math

guess = input("Who will win? ")

pygame.init()
size = pygame.display.set_mode()
screen_size = size.get_size()

screen = pygame.display.set_mode([screen_size[1], screen_size[1]])

screen.fill("cyan")
screen_size = screen.get_size()

pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2)], screen_size[1]/2)
pygame.draw.circle(screen, "pink", [screen_size[0]/2, (screen_size[1]/2)], screen_size[1]/2 - 5)

dimensions1 = [(0), (screen_size[1] / 2), (screen_size[0]), 5]
dimensions2 = [(screen_size[0]/2), (0), 5, screen_size[1]]

pygame.draw.rect(screen, "black", dimensions1)
pygame.draw.rect(screen, "black", dimensions2)

pygame.display.flip()
pygame.time.wait(2000)

p1score = 0
p2score = 0

for _ in range(10):

    p1x = random.randrange(0, screen_size[0])
    p1y = random.randrange(0, screen_size[1])

    p2x = random.randrange(0, screen_size[0])
    p2y = random.randrange(0, screen_size[1])

    distance_from_center1 = math.hypot(p1x-(screen_size[0]/2), p1y-(screen_size[1]/2))
    is_in_circle1 = distance_from_center1 <= (screen_size[1] / 2)

    distance_from_center2 = math.hypot(p2x-(screen_size[0]/2), p2y-(screen_size[1]/2))
    is_in_circle2 = distance_from_center2 <= (screen_size[1] / 2)

    if is_in_circle1:
        color1 = "lightgreen"
        p1score += 1
    else:
        color1 = "pink"

    if is_in_circle2:
        color2 = "green"
        p2score += 1
    else:
        color2 = "red"

    pygame.draw.circle(screen, color1, [p1x, p1y], 5)
    pygame.draw.circle(screen, color2, [p2x, p2y], 5)
    pygame.display.flip()
    pygame.time.wait(1000)


print("Score: " + str(p1score) + "-" + str(p2score))

if p1score > p2score:
    print("Player 1 Wins!")
    winner = "1"
else:
    print("Player 2 Wins!")
    winner = "2"

if guess == winner:
    print("You guessed correctly!")
else:
    print("Your guess was incorrect.")
