import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """管理飞船所发射子弹的类"""
  def __init__(self,ai_game):
    """在飞船当前位置创建一个子弹对象"""
    super().__init__()
    self.screen =  ai_game.screen
    self.settings = ai_game.settings
    
    # 在（0，0）创建一个表示子弹的矩形，在设置到正确位置
    self.image = pygame.image.load(self.settings.bullet_image)
    self.rect = self.image.get_rect()
    self.rect.midtop = ai_game.ship.rect.midtop
    
    # 存储用浮点数表示的子弹位置
    self.y = float(self.rect.y)

  def update(self):
    """向上移动子弹"""
    # 更新子弹的准确位置
    self.y -= self.settings.bullet_speed
    self.rect.y = self.y
  
  def draw_bullet(self):
    """在屏幕是绘制子弹"""
    self.screen.blit(self.image,self.rect)