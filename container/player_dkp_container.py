
from model.player_dkp import PlayerDKP
from exceptions.validation_error import EmptyDKPlist

class PlayerDkpContainer:

    def __init__(self, dkp_date, ignore_list=None):
        self.dkp_date = dkp_date
        self.player_dkp_list = []
        self.ignore_list = ignore_list or [] 

    def add(self, player_dkp: PlayerDKP):
        if not isinstance(player_dkp, PlayerDKP):
            print("Invalid player_dkp object")
            return

        if player_dkp.player_name in self.ignore_list:
            print(f"Player {player_dkp.player_name} is in the ignore list, skipping...")
            return
        
        self.player_dkp_list.append(player_dkp)
        
    def _get_list_sorted(self):
        self.player_dkp_list.sort(key=lambda x: x.player_name) 
        return self.player_dkp_list
    
    def validate(self):
        if not (self.player_dkp_list):
            raise EmptyDKPlist()

    def __str__(self):
        roster = "\n".join(str(player) for player in self._get_list_sorted())
        return f'**Roster ({self.dkp_date}):**\n{roster}'
    
