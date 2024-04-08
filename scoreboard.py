import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    '''显示得分信息的表'''

    def __init__(self, ai_game):
        '''初始化显示得分涉及的属性'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Segoe UI', 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分渲染为图像'''
        score_str = f'{round(self.stats.score, -1):,}'
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 16
        self.score_rect.top = 16

    def show_score(self):
        '''在屏幕上显示得分等'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        '''将最高分渲染为图像'''
        high_score_str = f'{round(self.stats.high_score, -1):,}'
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''检查是否诞生了新的最高分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        '''将等级渲染为图像'''
        level_str = 'Lv.' + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 16

    def prep_ships(self):
        '''显示还余下多少艘飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game, True)
            ship.rect.x = 16 + ship_number * ship.rect.width
            ship.rect.y = 16
            self.ships.add(ship)
