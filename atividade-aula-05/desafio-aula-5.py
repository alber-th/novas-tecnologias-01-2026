import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivência")
CLOCK = pygame.time.Clock()

# Fontes para o HUD e Game Over
fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)

class EntidadeBase:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):
        return self.rect.colliderect(outra.rect)

class Jogador(EntidadeBase):
    def __init__(self, x, y):
        # cor alterada
        super().__init__(x, y, 50, 50, (50, 150, 255))
        self.velocidade = 5

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.x < 750:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.y < 550:
            self.rect.y += self.velocidade

class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3, vida=3):
        # cor alterada
        super().__init__(x, y, 40, 40, (220, 80, 80))
        self.velocidade = velocidade
        self.vida = vida

    def perseguir(self, alvo):
        if self.rect.x < alvo.rect.x:
            self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x:
            self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y:
            self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y:
            self.rect.y -= self.velocidade

class EinimigoRapido(Inimigo):
    def __init__(self, x, y, velocidade_base=3, vida=3):
        # velocidade dobrada
        super().__init__(x, y, velocidade_base * 2, vida)
        self.cor = (255, 180, 50)

class EinimigoGigante(Inimigo):
    def __init__(self, x, y, velocidade=2, vida=5):
        super().__init__(x, y, velocidade, vida)
        self.rect.width = 80
        self.rect.height = 80
        self.cor = (150, 80, 255)

class Projetil(EntidadeBase):
    def __init__(self, x, y):
        super().__init__(x, y, 8, 15, (255, 255, 0))
        self.velocidade = -10

    def atualizar(self):
        self.rect.y += self.velocidade

def desenhar_hud(tela, estado):
    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    tela.blit(texto_pont, (10, 10))

    texto_vidas = fonte_normal.render(f"Vidas: {estado['vidas']}", True, (255, 255, 255))
    tela.blit(texto_vidas, (10, 40))

    texto_nivel = fonte_normal.render(f"Nível: {estado['nivel']}", True, (255, 255, 255))
    tela.blit(texto_nivel, (10, 70))

def desenhar_game_over(tela):
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render("GAME OVER", True, (255, 60, 60))
    tela.blit(texto, texto.get_rect(center=(400, 300)))

def desenhar_mensagem_nivel(tela, nivel):
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render(f"Nível {nivel}!", True, (80, 255, 80))
    tela.blit(texto, texto.get_rect(center=(400, 300)))

# Configuração de níveis
config_niveis = {
    1: {"vel_inimigo": 2, "qtd_iniciais": 4},
    2: {"vel_inimigo": 3, "qtd_iniciais": 6},
    3: {"vel_inimigo": 4, "qtd_iniciais": 8},
}

def criar_inimigo_aleatorio(nivel):
    tipo = random.choice(["normal", "rapido", "gigante"])
    vel_base = config_niveis[nivel]["vel_inimigo"]
    x = random.randint(0, 750)
    y = random.randint(0, 100)
    if tipo == "normal":
        return Inimigo(x, y, vel_base, vida=3)
    elif tipo == "rapido":
        return EinimigoRapido(x, y, velocidade_base=vel_base, vida=3)
    else:
        return EinimigoGigante(x, y, velocidade=max(1, vel_base - 1), vida=5)

# ==========================================
# Configuração inicial do Mini-Game
# ==========================================
jogador = Jogador(375, 275)

estado = {
    "pontuacao": 0,
    "vidas": 5,
    "rodando": True,
    "nivel": 1,
    "mensagem_nivel_ate": 0
}

inimigos = []
nivel_atual = estado["nivel"]
for _ in range(config_niveis[nivel_atual]["qtd_iniciais"]):
    inimigos.append(criar_inimigo_aleatorio(nivel_atual))

projeteis = []
timer_spawn = 0
tempo_entre_spawns = 300

while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                # Cria projétil a partir do centro superior do jogador
                proj_x = jogador.rect.centerx - 4
                proj_y = jogador.rect.top
                projeteis.append(Projetil(proj_x, proj_y))

    # Atualizar
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)

    # Atualiza inimigos e colisão com jogador
    for ini in inimigos[:]:
        ini.perseguir(jogador)
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            ini.rect.topleft = (random.randint(0, 750), 0)
            if estado["vidas"] <= 0:
                estado["rodando"] = False

    # Atualizar projeteis e colisão com inimigos
    for proj in projeteis[:]:
        proj.atualizar()
        if proj.rect.bottom < 0:
            projeteis.remove(proj)
            continue
        for ini in inimigos[:]:
            if proj.colidiu_com(ini):
                ini.vida -= 1
                if proj in projeteis:
                    projeteis.remove(proj)
                if ini.vida <= 0 and ini in inimigos:
                    inimigos.remove(ini)
                    estado["pontuacao"] += 20
                break

    # Spawn de novos inimigos a cada 300 frames
    timer_spawn += 1
    if timer_spawn % tempo_entre_spawns == 0:
        inimigos.append(criar_inimigo_aleatorio(estado["nivel"]))
        estado["pontuacao"] += 50

    estado["pontuacao"] += 1  # +1 ponto por frame sobrevivido

    # Sistema de níveis: a cada 500 pontos, avança nível
    max_nivel = max(config_niveis.keys())
    novo_nivel = min(1 + estado["pontuacao"] // 500, max_nivel)
    if novo_nivel > estado["nivel"]:
        estado["nivel"] = novo_nivel
        # adiciona alguns inimigos extras ao subir de nível
        for _ in range(2):
            inimigos.append(criar_inimigo_aleatorio(estado["nivel"]))
        # agenda mensagem de nível por 2 segundos
        estado["mensagem_nivel_ate"] = pygame.time.get_ticks() + 2000

    # Renderizar
    TELA.fill((20, 20, 40))
    jogador.desenhar(TELA)

    for ini in inimigos:
        ini.desenhar(TELA)

    for proj in projeteis:
        proj.desenhar(TELA)

    desenhar_hud(TELA, estado)

    # Exibe mensagem de mudança de nível por 2 segundos
    agora = pygame.time.get_ticks()
    if agora < estado["mensagem_nivel_ate"]:
        desenhar_mensagem_nivel(TELA, estado["nivel"])

    pygame.display.flip()
    CLOCK.tick(60)

# Fim de jogo
desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()