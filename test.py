import pygame


def run(screen=None):
    print('[main] run')

    if not screen:
        pygame.init()
        screen = pygame.display.set_mode((800,600))

    mainloop(screen)

def mainloop(screen):
    print('[main] mainloop')

    running = True
    while running:

        print('running game ...')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() # skip rest of code
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return  # go back to menu

        screen.fill((0,255,0))
        pygame.display.flip()

if __name__ == '__main__':
    run()