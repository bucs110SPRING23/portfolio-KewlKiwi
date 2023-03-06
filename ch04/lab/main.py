import random
import pygame
import math

pygame.init()
screen = pygame.display.set_mode()

width, height = pygame.display.get_window_size()

hitbox_width = width / 2
hitbox_height = height / 2

hitboxes = {
"red" : pygame.Rect(0, 0, hitbox_width, height),
"blue" : pygame.Rect(0, 0, hitbox_width, height)
}

hitboxes["blue"].topleft = hitboxes["red"].topright

main_colors = {
    "red" : (150, 0, 0),
    "blue" : (0, 0, 150)
    }
highlight_colors = {
    "red" : (255, 0, 0),
    "blue" : (0, 0, 255)
}

font = pygame.font.Font(None, 60)
done = False
quit = False
result = []
turns = 0
keys = hitboxes.keys()
order = list(keys)

screen.fill("lightgreen")

text = font.render("Welcome to Betting on Darts!", True, "black")
screen.blit(text, (hitbox_width - 250, hitbox_height - 100))

text = font.render("(Press Space to Begin)", True, "black")
screen.blit(text, (hitbox_width - 180, hitbox_height))

pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.QUIT == event.type:
             done = True
            elif event.key == pygame.K_SPACE:
                turns = len(order)
                result = []
                for color in order:
                    for c, hb in hitboxes.items():
                        pygame.draw.rect(screen, main_colors[c], hb)
                        dimensions1 = [hitbox_width - 190, hitbox_height - 15, 350, 70]
                        pygame.draw.rect(screen, "black", dimensions1)
                        text = font.render("Place Your Bet", True, "white")
                        screen.blit(text, (hitbox_width - 160, hitbox_height))
                    pygame.display.flip()
            elif event.key == pygame.K_q:
                     done = True
                     quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["red"].collidepoint(event.pos):
                pygame.draw.rect(screen, highlight_colors["red"], hitboxes["red"])
                dimensions1 = [hitbox_width - 190, hitbox_height - 15, 350, 70]
                pygame.draw.rect(screen, "black", dimensions1)
                text = font.render("Place Your Bet", True, "white")
                screen.blit(text, (hitbox_width - 160, hitbox_height))
                guess = "1"
                pygame.display.flip()
                pygame.time.delay(1000)
                done = True
            if hitboxes["blue"].collidepoint(event.pos):
                pygame.draw.rect(screen, highlight_colors["blue"], hitboxes["blue"])
                dimensions1 = [hitbox_width - 190, hitbox_height - 15, 350, 70]
                pygame.draw.rect(screen, "black", dimensions1)
                text = font.render("Place Your Bet", True, "white")
                screen.blit(text, (hitbox_width - 160, hitbox_height))
                guess = "2"
                pygame.display.flip()
                pygame.time.delay(1000)
                done = True

if not quit:
    size = pygame.display.set_mode()
    screen_size = size.get_size()

    screen.fill("cyan")
    screen_size = screen.get_size()

    pygame.draw.circle(screen, "black", [screen_size[0]/2, (screen_size[1]/2)], screen_size[1]/2)
    pygame.draw.circle(screen, "pink", [screen_size[0]/2, (screen_size[1]/2)], screen_size[1]/2 - 5)

    dimensions1 = [(0), (screen_size[1] / 2), (screen_size[0]), 5]
    dimensions2 = [(screen_size[0]/2), (0), 5, screen_size[1]]

    pygame.draw.rect(screen, "black", dimensions1)
    pygame.draw.rect(screen, "black", dimensions2)

    pygame.display.flip()
    pygame.time.wait(1000)

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
            color1 = "red"
            p1score += 1
        else:
            color1 = "pink"

        if is_in_circle2:
            color2 = "blue"
            p2score += 1
        else:
            color2 = "lightblue"

        pygame.draw.circle(screen, color1, [p1x, p1y], 5)
        pygame.draw.circle(screen, color2, [p2x, p2y], 5)
        pygame.display.flip()
        pygame.time.wait(1000)

    pygame.display.flip()
    pygame.time.delay(1000)

    screen.fill("lightgreen")

    text = font.render(("Score: " + str(p1score) + "-" + str(p2score)), True, "black")
    screen.blit(text, (hitbox_width - 130, hitbox_height - 80))

    if p1score == p2score:
        text = font.render("It's a Tie!", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height))
        winner = "tie"
    elif p1score > p2score:
        text = font.render("Red Wins!", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height))
        winner = "1"
    else:
        text = font.render("Blue Wins!", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height))
        winner = "2"

    if guess == winner:
        text = font.render("You guessed correctly!", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height + 80))
    else:
        text = font.render("Your guess was incorrect.", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height + 80))

    if p1score == p2score:
        text = font.render("(Because they tied, Sorry!)", True, "black")
        screen.blit(text, (hitbox_width - 130, hitbox_height + 140))

    pygame.display.flip()
    pygame.time.delay(2000)
