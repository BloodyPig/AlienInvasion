class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,250,250)
        self.ship_speed_factor = 3
        self.ship_limit = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1:右移 -1:左移
        self.fleet_direction = 1