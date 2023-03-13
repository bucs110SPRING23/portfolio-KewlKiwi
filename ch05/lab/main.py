import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int((3 * n) + 1)
    return count

def threenp1range(upper_limit):
  objs_in_sequence = []
  for _ in range(2, upper_limit + 1):
     objs_in_sequence.append((_, threenp1(_)))
  #objs_in_sequence = { n => iters}
  return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
  pygame.init()
  display = pygame.display.set_mode()
  new_display = pygame.transform.flip(display, False, True)
  width, height = new_display.get_size()
  new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
  length = len(threenplus1_iters_dict)
  new_display.fill("black")

  max_so_far = int(threenplus1_iters_dict[0][1])

  for _ in range(length - 1):
     if max_so_far < int(threenplus1_iters_dict[_][1]):
         max_so_far = int(threenplus1_iters_dict[_][1])
     msg = ("Max So Far: " + str(max_so_far))

     display.blit(new_display, (0, 0))
     
     font = pygame.font.Font(None, 60)
     msg = font.render(msg, True, "white")
     display.blit(msg, [100, 500])

     pygame.draw.lines(new_display, "white", (100, 900), ((threenplus1_iters_dict[_]), (threenplus1_iters_dict[_ + 1])))

     pygame.display.flip()
     pygame.time.delay(10)



def main():
  upper_limit = int(input("Please enter an upper limit: "))
  threenplus1_iters_dict = (threenp1range(upper_limit))
  graph_coordinates(threenplus1_iters_dict)

main()