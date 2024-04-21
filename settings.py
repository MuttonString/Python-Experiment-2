class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.fullscreen = False
        self.tick = 60
        self.bg_color = (224, 224, 224)
        self.bg_image = True

        self.ship_speed = 3.5
        self.ship_limit = 3
        self.ship_width = 64
        self.ship_height = 80

        self.bullet_speed = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (119, 67, 66)
        self.bullets_allowed = 5

        self.alien_width = 64
        self.alien_height = 64
        self.alien_speed = 2.5
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.alien_points = 50

        self._set_default()

    def _set_default(self):
        '''记忆随游戏进行而变化的设置的初始值'''
        self.default_ship_speed = self.ship_speed
        self.default_bullet_speed = self.bullet_speed
        self.default_alien_speed = self.alien_speed
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = self.default_ship_speed
        self.bullet_speed = self.default_bullet_speed
        self.alien_speed = self.default_alien_speed
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置的值和外星人分数'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
