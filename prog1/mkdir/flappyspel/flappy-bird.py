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

class Fågel:
    def __init__(self):
        self.x = 50
        self.y = SKÄRM_HÖJD // 2
        self.gravitation = 0.50
        self.lyft = -10
        self.hastighet = 0
        
    def visa(self):
        pygame.draw.circle(skärm, SVART, (self.x, self.y), 20)
    def uppdatera(self):
        self.hastighet += self.gravitation
        self.hastighet *= 0.9
        self.y += self.hastighet

        if self.y > SKÄRM_HÖJD:
            self.y = SKÄRM_HÖJD
            self.hastighet = 0
        if self.y < 0:
            self.y = 0
            self.hastighet = 0

    def hoppa(self):
        self.hastighet += self.lyft
        
class Rör:
    def __init__(self):
        self.x = SKÄRM_BREDD
        self.glugg = 200
        self.över = random.randint(100, SKÄRM_HÖJD - self.glugg - 100)
        self.under = self.över + self.glugg
        self.hastighet = 0
        self.rör_bredd = 50
        self.poängad = False
        
    def visa(self):
        pygame.draw.rect(skärm, GRÖN, (self.x, 0, self.rör_bredd, self.över))
        pygame.draw.rect(skärm, GRÖN, (self.x, self.under, self.rör_bredd, SKÄRM_HÖJD - self.under))

    def uppdatera(self):
        self.x -= self.hastighet

def skapa_rör():
    rör = []
    for _ in range(5):
        nytt_rör = Rör()
        nytt_rör.hastighet = rör_hastighet
        rör.append(nytt_rör)
    return rör

def huvud(spel_nivå):
    fågel = Fågel()
    poäng = 0
    global rör_hastighet
    if spel_nivå == "enkel":
        rör_hastighet = 2
    elif spel_nivå == "medel":
        rör_hastighet = 4
    elif spel_nivå == "svår":
        rör_hastighet = 6

    rör = skapa_rör()

    score_font = pygame.font.Font(None, 36)

    while True:
        for händelse in pygame.event.get():
            if händelse.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if händelse.type == pygame.KEYDOWN:
                if händelse.key == pygame.K_SPACE:
                    fågel.hoppa()

        fågel.uppdatera()

        
        if rör[-1].x < SKÄRM_BREDD - 200:
            rör.append(Rör())
            rör[-1].hastighet = rör_hastighet

        
        for röret in rör:
            röret.uppdatera()

            
        if fågel.x + 20 > röret.x and fågel.x - 20 < röret.x + röret.rör_bredd:
                if fågel.y - 20 < röret.över or fågel.y + 20 > röret.under:
                    print("Spelet är över! Din poäng:", poäng)
                    pygame.quit()
                    sys.exit()
        if fågel.x + 20 > röret.x and fågel.x - 20 < röret.x + röret.rör_bredd:
                if fågel.y - 20 < röret.över or fågel.y + 20 > röret.under:
                    print("Spelet är över! Din poäng:", poäng)
                    pygame.quit()
                    sys.exit()

            
        if röret.x + röret.rör_bredd < fågel.x - 20 and not röret.poängad:
                röret.poängad = True
                poäng += 1
                print("Poäng:", poäng)
