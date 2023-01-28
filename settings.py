class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        self.alien_speed      = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1 # 1 -> right | -1 -> left

        self.screen_width  = 1600
        self.screen_height = 1200
        #self.bg_color      = (180, 180, 180)
        self.bg_color      = (230, 230, 230)

        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullets
        self.bullet_speed    = 1.5
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (60, 60, 60)
        self.bullets_allowed = 3  # Limit the number of bullets
