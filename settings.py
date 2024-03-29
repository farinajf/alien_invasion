class Settings:
    """A class to store all settings for Alien Invasion."""

    #************************************************************************#
    #                          __init__(self)                                #
    #************************************************************************#
    def __init__(self):

        self.screen_width  = 1600
        self.screen_height = 1200
        #self.bg_color      = (180, 180, 180)
        self.bg_color      = (230, 230, 230)

        self.ship_limit = 3

        #Bullets
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (60, 60, 60)
        self.bullets_allowed = 3  # Limit the number of bullets

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale   = 1.5

        self.initialize_dynamic_settings()


    #************************************************************************#
    #                initialize_dynamic_settings(self)                       #
    #************************************************************************#
    def initialize_dynamic_settings(self):

        self.ship_speed   = 1.5
        self.bullet_speed = 3.0
        self.alien_speed  = 1.0

        self.fleet_direction = 1

        self.alien_points = 50


    #************************************************************************#
    #                      increase_speed(self)                              #
    #************************************************************************#
    def increase_speed(self):

        self.ship_speed   *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed  *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
