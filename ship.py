import pygame
from settings import Settings

class Ship:
  """管理飞船的类"""
  def __init__(self,ai_game):
    """初始化飞船并设置其初始位置"""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.settings = ai_game.settings
    
    # 加载飞船图像并获取其外接矩形
    self.image = pygame.image.load('./imgs/plane.png')
    self.rect = self.image.get_rect()
    
    # 每艘新飞船都放在屏幕底部的中央
    self.rect.midbottom = self.screen_rect.midbottom
    
    #移动标识
    self.moving_right = False
    self.moving_left = False
    self.moving_top = False
    self.moving_bottom = False
    
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
  
  def blitme(self):
    """在指定位置绘制飞船"""
    self.screen.blit(self.image,self.rect)
    
  def update(self):
    """根据移动标志调整飞船位置"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
      self.rect.x = self.x
    elif self.moving_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed
      self.rect.x = self.x
    elif self.moving_top and self.rect.top > 0:
      self.y -= self.settings.ship_speed
      self.rect.y = self.y
    elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
      self.y += self.settings.ship_speed
      self.rect.y = self.y
  
    
  