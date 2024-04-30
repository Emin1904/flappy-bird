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
