import pygame

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
