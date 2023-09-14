## Original Code Attribution

This project is based on the code examples and exercises from the book **Python Crash Course** by Eric Matthes. The original code can be found in the book.

- Book Title: [Python Crash Course](https://github.com/ehmatthes/pcc.git)
- Author: Eric Matthes
- Publisher: No Starch Press
- Description: In Alien Invasion, the player controls a ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

Please refer to the book for the original code and explanations.

### Modifications I made to the code

The original code deleted the high score every time the user closed the game. I modified the code so the high score is saved to a file on the device. This ensures the high score is not reset every time the player starts a new game.
###### game_stats.py
```python
def __init__(self, ai_settings):
    self.get_high_score()

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
```

The original code made the players press the spacebar to fire the bullets to shoot the aliens. I wanted to focus more on the movement of the player ship so I modified the code to automatically fire the bullets.
###### game_functions.py
I commented out the line of code where the spacebar is a key-down event

