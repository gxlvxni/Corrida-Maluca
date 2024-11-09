import pygame
import random

pygame.init()
tamanho = (1000, 592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255, 255, 255)
fundo = pygame.image.load("assets/fundo.png")
fundo_vitoria = pygame.image.load("assets/fundo_vitoria.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
carro3 = pygame.image.load("assets/carro3.png")

movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 30
posYCar2 = 120
posYCar3 = 210
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1)
acabou = False
somDaVitoria = False
vencedor = None

def exibir_ranking(distancias):
    tela.fill(branco)
    tela.blit(fundo_vitoria, (0, 0))
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    
   
    carros = [("Vermelho", distancias[0]), ("Amarelo", distancias[1]), ("Azul", distancias[2])]
    carros.sort(key=lambda x: x[1], reverse=True)  

  
    for i, (cor, distancia) in enumerate(carros):
        texto = fonte.render(f"{i+1}º - {cor} - {distancia} metros", True, branco)
        tela.blit(texto, (370, 100 + i * 50))
    
    pygame.display.update()
    pygame.time.delay(5000)  

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (movXCar1, posYCar1))
    tela.blit(carro2, (movXCar2, posYCar2))
    tela.blit(carro3, (movXCar3, posYCar3))

    if not acabou:
        movXCar1 += random.randint(0, 10)
        movXCar2 += random.randint(0, 10)
        movXCar3 += random.randint(0, 10)
    else:
        pygame.mixer.music.stop()
        if not somDaVitoria:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True

    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 310

    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 410

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 500

    if not acabou:
        if posYCar1 == 310 and movXCar1 >= 900 and movXCar1 > movXCar2 and movXCar1 > movXCar3:
            vencedor = "Vermelho"
            acabou = True
        elif posYCar2 == 410 and movXCar2 >= 900 and movXCar2 > movXCar1 and movXCar2 > movXCar3:
            vencedor = "Amarelo"
            acabou = True
        elif posYCar3 == 500 and movXCar3 >= 900 and movXCar3 > movXCar1 and movXCar3 > movXCar2:
            vencedor = "Azul"
            acabou = True

        distancias = [movXCar1, movXCar2, movXCar3]
        primeiro_colocado = max(distancias)
        segundo_colocado = sorted(distancias)[-2]
        terceiro_colocado = sorted(distancias)[2]
        distancia_para_segundo = primeiro_colocado - segundo_colocado
        distancia_para_terceiro = segundo_colocado - terceiro_colocado

        fonte = pygame.font.Font("freesansbold.ttf", 30)
        texto = fonte.render(f"Vencendo: {distancias.index(primeiro_colocado) + 1} - Distância para 2º: {distancia_para_segundo}  Distância para 3º: {distancia_para_terceiro}", True, branco)
        tela.blit(texto, (120, 20))
    else:
        tela.fill( branco )
        tela.blit(fundo_vitoria,(0,0))
 
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

