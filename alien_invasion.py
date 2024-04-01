import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
  """管理游戏资源和行为的类"""
  def __init__(self):
    """初始化游戏并创建游戏资源"""
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((
      self.settings.screen_width,self.settings.screen_height
    ))
    pygame.display.set_caption('Alien Invasion')
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
  
  def run_game(self):
    """开始游戏的主循环"""
    while True:
      self._check_events()
      self.ship.update()
      self._update_bullets()
      self._update_screen()
      self.clock.tick(60)
  
  def _check_events(self):
     # 侦听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
          self._check_keyup_events(event)        
  
  def _update_screen(self):
    # 更新页面
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.ship.blitme()
    pygame.display.flip()
  
  def _check_keydown_events(self,event):
    if event.key == pygame.K_d:
      self.ship.moving_right = True
    elif event.key == pygame.K_a:
      self.ship.moving_left = True
    elif event.key == pygame.K_w:
      self.ship.moving_top = True
    elif event.key == pygame.K_s:
      self.ship.moving_bottom = True
    elif event.key == pygame.K_ESCAPE:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
  
  def _check_keyup_events(self,event):
    if event.key == pygame.K_d:
      self.ship.moving_right = False
    elif event.key == pygame.K_a:
      self.ship.moving_left = False
    elif event.key == pygame.K_w:
      self.ship.moving_top = False
    elif event.key == pygame.K_s:
      self.ship.moving_bottom = False
    
  def _fire_bullet(self):
    """创建一颗子弹，并将其加入编组bullets"""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)
  
  def _update_bullets(self):
    #  更新子弹位置
    self.bullets.update()
      # 删除已经消失的子弹
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()