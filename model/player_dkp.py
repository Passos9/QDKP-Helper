import re

class PlayerDKP:
    
    def __init__(self, player, total, total_spent):
        if total == 0:
            raise ValueError() # Player never was in a DKP session
        
        self.player_name = player
        self.net = total - total_spent
        self.total = total
        
            
    def __str__(self):
        return f"Player: {self.player_name}, Net: {self.net}, Total: {self.total}"