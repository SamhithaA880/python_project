import os

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.high_score  = 0
        
        self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score      = 0
        self.level      = 1
    
    def get_high_score(self):
        """Search for the file with highscore."""
        path = './highscore.txt'
        if os.path.exists(path):
            f = open("highscore.txt", 'r')
            content         = f.read()
            content         = int(content)
            f.close()
            self.high_score = content
        else:
            f = open("highscore.txt", 'w')
            f.write(str(self.high_score))
            f.close()
            
            # Define permission modes
            new_permissions = 0o600
            # Set the new permissions for the file
            os.chmod(path, new_permissions)
