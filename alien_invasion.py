import sys
import pygame

class AlienInvasion:
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('外星人入侵')
        self.bg_color = (55, 125, 34)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 侦听键鼠事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时重绘屏幕
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    AlienInvasion().run_game()