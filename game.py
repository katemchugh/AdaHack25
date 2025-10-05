import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dress to Reflect")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (80, 150, 255)
BROWN = (139, 69, 19)
GRAY = (180, 180, 180)
RED = (255, 100, 100)
GREEN = (100, 200, 100)

# Fonts
font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

# Game states
STATE_CHOOSE = "choose"
STATE_IMPACT = "impact"
state = STATE_CHOOSE

# Outfits as colored rectangles
outfits = [
    {"name": "Floral Dress", "color": (255, 182, 193)},
    {"name": "Denim Jeans", "color": (100, 149, 237)},
    {"name": "Leather Jacket", "color": (50, 50, 50)},
]

chosen_outfit = None
impacts = [
    "💧 The river is polluted from dye runoff.",
    "🔥 It’s hotter — factories are burning energy nonstop.",
    "🗑️ Mountains of clothing waste pile up nearby."
]
impact_index = 0
clock = pygame.time.Clock()


def draw_text_center(text, y, font, color=BLACK):
    """Draw centered text on screen."""
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)


def draw_choose_screen():
    screen.fill(WHITE)
    draw_text_center("Pick an Outfit!", 80, font)
    for i, outfit in enumerate(outfits):
        rect = pygame.Rect(150 + i * 200, 200, 120, 180)
        pygame.draw.rect(screen, outfit["color"], rect)
        draw_text_center(outfit["name"], rect.y + 210, small_font)


def draw_impact_screen():
    global impact_index
    # Background darkens to reflect environmental damage
    screen.fill((100, 100, 120))
    draw_text_center("Unchosen clothes were shipped overseas...", 100, font, WHITE)
    draw_text_center(impacts[impact_index], 300, small_font, WHITE)
    draw_text_center("(Press SPACE to continue)", 500, small_font, GRAY)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == STATE_CHOOSE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check which outfit was clicked
                for i, outfit in enumerate(outfits):
                    rect = pygame.Rect(150 + i * 200, 200, 120, 180)
                    if rect.collidepoint(x, y):
                        chosen_outfit = outfit
                        state = STATE_IMPACT
                        break

        elif state == STATE_IMPACT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    impact_index += 1
                    if impact_index >= len(impacts):
                        # End message
                        screen.fill(BLACK)
                        draw_text_center("😔 The people there suffer.", 250, font, WHITE)
                        draw_text_center("💭 Maybe fashion can be fair and sustainable.", 350, small_font, GRAY)
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False

    if state == STATE_CHOOSE:
        draw_choose_screen()
    elif state == STATE_IMPACT:
        draw_impact_screen()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
