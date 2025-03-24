from model.player_item import PlayerItem
from exceptions.validation_error import EmptyPlayerItemlist

class PlayerItemContainer:

    def __init__(self, raid_name, raid_date):
        self.raid_date = raid_date
        self.raid_name = raid_name
        self.player_item_list = []

    def add(self, player_item: PlayerItem):
        if isinstance(player_item, PlayerItem):
            self.player_item_list.append(player_item)
           
        else:
            print("Invalid player_dkp object")

    def _get_list_sorted(self):
        self.player_item_list.sort(key=lambda x: x.player_name) 
        return self.player_item_list

    def validate(self):
        if not (self.player_item_list):
            raise EmptyPlayerItemlist()
        
    def __str__(self):
        loot = "\n".join(str(player_item) for player_item in self._get_list_sorted())
        return f'**{self.raid_name} loot- {self.raid_date}:**\n{loot}'
