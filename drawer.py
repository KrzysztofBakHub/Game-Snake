import pygame

from config import CONFIG, COLORS

class Drawer:
    def __init__(self, width, height):
        pygame.font.init()
        self.screen = pygame.display.set_mode([width, height])
        self.score_font = pygame.font.SysFont("arial", 24)
        self.title_font = pygame.font.SysFont("arial", 48, bold=True)
        self.hint_font = pygame.font.SysFont("arial", 22)

    def drawGrid(self):
        sizeBtw = CONFIG["width"] // CONFIG["rows"]

        for i in range(CONFIG["rows"]):
            x = i * sizeBtw
            y = i * sizeBtw

            pygame.draw.line(self.screen, COLORS["white"], (x, 0), (x, CONFIG["width"]))
            pygame.draw.line(self.screen, COLORS["white"], (0, y), (CONFIG["width"], y))

    def drawWindow(self):
        self.screen.fill(COLORS["black"])
        self.drawGrid()

    def drawRect(self, rect):
        dis = CONFIG["width"] // CONFIG["rows"]
        pos = rect.getPos()
        i = pos[0]
        j = pos[1]

        pygame.draw.rect(self.screen, rect.getColor(), (i * dis + 1, j * dis + 1, dis - 1, dis - 1))

    def draw_score(self, score):
        score_surface = self.score_font.render(f"Score: {score}", True, COLORS["white"])
        self.screen.blit(score_surface, (10, 10))

    def draw_post_game_info(self, score):
        overlay = pygame.Surface((CONFIG["width"], CONFIG["width"]))
        overlay.set_alpha(180)
        overlay.fill(COLORS["black"])
        self.screen.blit(overlay, (0, 0))

        game_over_surface = self.title_font.render("GAME OVER", True, COLORS["red"])
        game_over_rect = game_over_surface.get_rect(center=(CONFIG["width"] // 2, 220))
        self.screen.blit(game_over_surface, game_over_rect)

        restart_surface = self.hint_font.render("Press R to restart", True, COLORS["white"])
        restart_rect = restart_surface.get_rect(center=(CONFIG["width"] // 2, 280))
        self.screen.blit(restart_surface, restart_rect)

        final_score_surface = self.hint_font.render(f"Final score: {score}", True, COLORS["white"])
        final_score_rect = final_score_surface.get_rect(center=(CONFIG["width"] // 2, 320))
        self.screen.blit(final_score_surface, final_score_rect)

    def update_window(self):
        pygame.display.update()
