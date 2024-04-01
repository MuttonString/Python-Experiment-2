class Settings:
  """存储游戏《外星人入侵》中所有设置的类"""
  def __init__(self):
    """初始化游戏的设置"""
    # 屏幕设置
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230,230,230)
    
    # 飞船速度设置
    self.ship_speed = 4.5
    
    # 子弹设置
    self.bullet_speed = 6
    self.bullet_image = 'imgs/basketball.png'
    self.bullets_allowed = 8
    