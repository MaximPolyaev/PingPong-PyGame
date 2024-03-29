import pygame
import random

KEY_BACKSPACE = 32
SIZE_WINDOW_X = 800
SIZE_WINDOW_Y = 400
CENTER_WINDOW_X = SIZE_WINDOW_X / 2
CENTER_WINDOW_Y = SIZE_WINDOW_Y / 2
BALL_SIZE_X = 50
BALL_SIZE_Y = 50
BALL_SPEED = 1
PLUS_BALL_SPEED = 0.5

# directions
RIGHT_TOP = 1
RIGHT_BOTTOM = 2
LEFT_BOTTOM = 3
LEFT_TOP = 4

window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
pygame.display.set_caption('Hello')
screen = pygame.Surface((SIZE_WINDOW_X, SIZE_WINDOW_Y))
check_point = pygame.Surface((5, 5))

pygame.font.init()
font_tap_play = pygame.font.SysFont('arial', 50)
textTapPlay = font_tap_play.render('Tap to Play', 1, (50, 50, 50))

font_score = pygame.font.SysFont('none', 70)
font_win = pygame.font.SysFont('none', 90)

class Game:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.left_player_win = False
        self.right_player_win = False

    def reset(self):
        self.left_score = 0
        self.right_score = 0
        ball.speed = BALL_SPEED
        ball.reset()

    def score_controller(self):
        if ball.pos_x > (SIZE_WINDOW_X + BALL_SIZE_X / 2) and ball.pos_y < SIZE_WINDOW_Y and ball.pos_y > 0:
            ball.status_tap = False
            self.left_score += 1
            ball.speed += PLUS_BALL_SPEED
            if self.left_score >= 10:
                self.left_player_win = True
                self.reset()
            else:
                ball.reset()
        elif ball.pos_x < (0 - BALL_SIZE_X / 2) and ball.pos_y < SIZE_WINDOW_Y and ball.pos_y > 0:
            ball.status_tap = False
            self.right_score += 1
            if self.right_score >= 10:
                self.right_player_win = True
                self.reset()
            else:
                ball.reset()

    @staticmethod
    def collision_controller():
        # top wall
        if ball.pos_top_left_y < 0:
            if ball.direction == RIGHT_TOP:
                ball.direction = RIGHT_BOTTOM
            elif ball.direction == LEFT_TOP:
                ball.direction = LEFT_BOTTOM
        # right wall
        # elif ball.pos_bottom_right_x > SIZE_WINDOW_X:
        #     if ball.direction == RIGHT_BOTTOM:
        #         ball.direction = LEFT_BOTTOM
        #     elif ball.direction == RIGHT_TOP:
        #         ball.direction = LEFT_TOP
        # bottom wall
        elif ball.pos_bottom_left_y > SIZE_WINDOW_Y:
            if ball.direction == RIGHT_BOTTOM:
                ball.direction = RIGHT_TOP
            elif ball.direction == LEFT_BOTTOM:
                ball.direction = LEFT_TOP
        # left wall
        # elif ball.pos_top_left_x < 0:
        #     if ball.direction == LEFT_BOTTOM:
        #         ball.direction = RIGHT_BOTTOM
        #     elif ball.direction == LEFT_TOP:
        #         ball.direction = RIGHT_TOP



class ControllerBall:
    def __init__(self, pos_x, pos_y, size_x, size_y, filename_img):
        self.status_tap = False
        self.speed = BALL_SPEED

        self.direction = random.randint(1, 4)

        self.default_pos_x = pos_x
        self.default_pos_y = pos_y

        self.pos_x_one = pos_x
        self.pos_x_two = 600
        self.pos_x = pos_x

        self.pos_y_one = pos_y
        self.pos_y_two = 0
        self.pos_y = pos_y

        self.pos_top_left_x = self.pos_x - BALL_SIZE_X / 2
        self.pos_top_left_y = self.pos_y - BALL_SIZE_Y / 2
        self.pos_top_right_x = self.pos_top_left_x + BALL_SIZE_X
        self.pos_top_right_y = self.pos_y - BALL_SIZE_Y / 2
        self.pos_bottom_left_x = self.pos_x - BALL_SIZE_X / 2
        self.pos_bottom_right_x = self.pos_bottom_left_x + BALL_SIZE_X
        self.pos_bottom_left_y = self.pos_top_left_y + BALL_SIZE_Y
        self.pos_bottom_right_y = self.pos_top_right_y + BALL_SIZE_Y

        self.bitmap = pygame.image.load(filename_img)
        self.bitmap = pygame.transform.scale(
            self.bitmap, (size_x, size_y))

    def render(self):
        screen.blit(self.bitmap, (self.pos_x - BALL_SIZE_X / 2, self.pos_y - BALL_SIZE_X / 2))

    def render_pos(self):
        if self.direction == RIGHT_TOP:
            self.pos_x += self.speed
            self.pos_y -= self.speed
        elif self.direction == RIGHT_BOTTOM:
            self.pos_y += self.speed
            self.pos_x += self.speed
        elif self.direction == LEFT_BOTTOM:
            self.pos_x -= self.speed
            self.pos_y += self.speed
        elif self.direction == LEFT_TOP:
            self.pos_x -= self.speed
            self.pos_y -= self.speed
        self.__update_positions()

    def reset(self):
        self.pos_x = self.default_pos_x
        self.pos_y = self.default_pos_y
        self.__update_positions()

    def __update_positions(self):
        self.pos_top_left_x = self.pos_x - BALL_SIZE_X / 2
        self.pos_top_left_y = self.pos_y - BALL_SIZE_Y / 2
        self.pos_top_right_x = self.pos_top_left_x + BALL_SIZE_X
        self.pos_top_right_y = self.pos_y - BALL_SIZE_Y / 2
        self.pos_bottom_left_x = self.pos_x - BALL_SIZE_X / 2
        self.pos_bottom_right_x = self.pos_bottom_left_x + BALL_SIZE_X
        self.pos_bottom_left_y = self.pos_top_left_y + BALL_SIZE_Y
        self.pos_bottom_right_y = self.pos_top_right_y + BALL_SIZE_Y


ball = ControllerBall(CENTER_WINDOW_X, CENTER_WINDOW_Y, BALL_SIZE_X, BALL_SIZE_Y, 'ball.png')
game = Game()

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYUP:
            if e.key == KEY_BACKSPACE:
                if game.left_player_win or game.right_player_win:
                    game.left_player_win = False
                    game.right_player_win = False
                ball.status_tap = True
    screen.fill((38, 37, 165))
    check_point.fill((127, 255, 0))

    pygame.draw.rect(screen, (180, 180, 180), (CENTER_WINDOW_X - 4, 0, 8, SIZE_WINDOW_Y))

    if not ball.status_tap:
        text_score_left = font_score.render(str(game.left_score), 1, (127, 255, 0))
        screen.blit(text_score_left, (CENTER_WINDOW_X - 50, 0))

        text_score_right = font_score.render(str(game.right_score), 1, (127, 255, 0))
        screen.blit(text_score_right, (CENTER_WINDOW_X + 24, 0))

        if game.left_player_win:
            text_win_left = font_win.render('WIN', 1, (240, 200, 240))
            screen.blit(text_win_left, (100, CENTER_WINDOW_Y - 100))
        if game.right_player_win:
            text_win_right = font_win.render('WIN', 1, (240, 200, 240))
            screen.blit(text_win_right, (CENTER_WINDOW_X + 170, CENTER_WINDOW_Y - 100))

        ball.direction = random.randint(1, 4)
        ball.render()
        screen.blit(textTapPlay, (CENTER_WINDOW_X - 100, CENTER_WINDOW_Y - 80))
        window.blit(screen, (0, 0))
        pygame.display.flip()
    else:
        text_score_left = font_score.render(str(game.left_score), 1, (127, 255, 0))
        screen.blit(text_score_left, (CENTER_WINDOW_X - 50, 0))

        text_score_right = font_score.render(str(game.right_score), 1, (127, 255, 0))
        screen.blit(text_score_right, (CENTER_WINDOW_X + 24, 0))

        ball.render()
        ball.render_pos()
        game.score_controller()
        game.collision_controller()

        screen.blit(check_point, (ball.pos_top_left_x, ball.pos_top_left_y))
        screen.blit(check_point, (ball.pos_top_right_x - 5, ball.pos_top_right_y))
        screen.blit(check_point, (ball.pos_bottom_left_x, ball.pos_bottom_left_y - 5))
        screen.blit(check_point, (ball.pos_bottom_right_x - 5, ball.pos_bottom_right_y - 5))
        screen.blit(check_point, (ball.pos_x - 2.5, ball.pos_y - 2.5))

        window.blit(screen, (0, 0))
        pygame.display.flip()
