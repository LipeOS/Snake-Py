import pygame
import random


# Inicialização do Pygame
pygame.init()

# Definição das cores
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Definição das configurações da tela
largura_tela = 800
altura_tela = 600
tamanho_bloco = 20

# Configurações da cobra
velocidade = 10

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')



# Função para mostrar o score
def mostrar_score(score, recorde):
    fonte = pygame.font.SysFont(None, 25)
    texto_score = fonte.render(f"Score: {score}", True, BRANCO)
    tela.blit(texto_score, (largura_tela - 120, 10))
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, BRANCO)
    tela.blit(texto_recorde, (largura_tela - 120, 40))

# Função principal do jogo
def jogo():
    sair = False
    game_over = False

    # Posição inicial da cobra
    cabeca_x = largura_tela / 2
    cabeca_y = altura_tela / 2
    cabeca_dx = 0
    cabeca_dy = 0

    # Lista para o corpo da cobra
    corpo_cobra = []
    comprimento_inicial = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20) * 20
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20) * 20

    # Score
    score = 0
    recorde = 0

    while not sair:
        while game_over:
            tela.fill(PRETO)
            fonte = pygame.font.SysFont(None, 30)
            texto = fonte.render("Game Over! Pressione R para jogar novamente ou Q para sair.", True, BRANCO)
            tela.blit(texto, (100, altura_tela / 2 - 25))
            mostrar_score(score, recorde)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair = True
                        game_over = False
                    if event.key == pygame.K_r:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cabeca_dx = -tamanho_bloco
                    cabeca_dy = 0
                elif event.key == pygame.K_RIGHT:
                    cabeca_dx = tamanho_bloco
                    cabeca_dy = 0
                elif event.key == pygame.K_UP:
                    cabeca_dx = 0
                    cabeca_dy = -tamanho_bloco
                elif event.key == pygame.K_DOWN:
                    cabeca_dx = 0
                    cabeca_dy = tamanho_bloco

        if cabeca_x >= largura_tela or cabeca_x < 0 or cabeca_y >= altura_tela or cabeca_y < 0:
            game_over = True

        cabeca_x += cabeca_dx
        cabeca_y += cabeca_dy

        tela.fill(PRETO)

        pygame.draw.rect(tela, PRETO, [largura_tela - 150, 0, 150, altura_tela])
        mostrar_score(score, recorde)

        pygame.draw.rect(tela, BRANCO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca = []
        cabeca.append(cabeca_x)
        cabeca.append(cabeca_y)
        corpo_cobra.append(cabeca)

        if len(corpo_cobra) > comprimento_inicial:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca:
                game_over = True

        for segmento in corpo_cobra:
            pygame.draw.rect(tela, VERMELHO, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        if cabeca_x == comida_x and cabeca_y == comida_y:
            score += 100
            if score > recorde:
                recorde = score
            comprimento_inicial += 1
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20) * 20
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20) * 20

        pygame.time.Clock().tick(velocidade)

    pygame.quit()
    quit()

jogo()
