import pygame
import sys
import random

pygame.init()

SKÄRM_BREDD = 400
SKÄRM_HÖJD = 600
VIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÖN = (0, 255, 0)
FPS = 60

skärm = pygame.display.set_mode((SKÄRM_BREDD, SKÄRM_HÖJD))
pygame.display.set_caption("Flappy Bird")

font = pygame.font.Font(None, 36)
enkel_text = font.render("Enkel", True, SVART)
medel_text = font.render("Medel", True, SVART)
svår_text = font.render("Svår", True, SVART)

enkel_rect = enkel_text.get_rect(center=(SKÄRM_BREDD // 2, SKÄRM_HÖJD // 2 - 50))
medel_rect = medel_text.get_rect(center=(SKÄRM_BREDD // 2, SKÄRM_HÖJD // 2))
svår_rect = svår_text.get_rect(center=(SKÄRM_BREDD // 2, SKÄRM_HÖJD // 2 + 50))

skärm.fill(VIT)
skärm.blit(enkel_text, enkel_rect)
skärm.blit(medel_text, medel_rect)
skärm.blit(svår_text, svår_rect)
pygame.display.update()

def välj_svårighetsnivå():
    while True:
        for händelse in pygame.event.get():
            if händelse.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if händelse.type == pygame.MOUSEBUTTONDOWN:
                mus_x, mus_y = pygame.mouse.get_pos()
                if enkel_rect.collidepoint(mus_x, mus_y):
                    return "enkel"
                elif medel_rect.collidepoint(mus_x, mus_y):
                    return "medel"
                elif svår_rect.collidepoint(mus_x, mus_y):
                    return "svår"
spel_nivå = välj_svårighetsnivå()

class fågel:
    def __init__(self):
        self.x = 50
        self.y = SKÄRM_HÖJD // 2
        self.gravitation = 0.50
        self.lyft = -10
        self.hastighet = 0
        
    def visa(self):
        pygame.draw.circle(skärm, SVART, (self.x, self.y), 20)


