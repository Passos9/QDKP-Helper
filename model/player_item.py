from utils.converters import item_to_wowhead_link, timestamp_to_datetime


class PlayerItem:
    
    def __init__(self, player_name, player_loot_entry, wow_data_url):
        if 2 in player_loot_entry[4]: # It contains the points spent
                    if (player_loot_entry[2] == None): # Gurantees there is an item associated with it 
                        raise ValueError()             # (it's possible to make players spend for nothing)
                    self.link_item = item_to_wowhead_link(player_loot_entry[2], wow_data_url)
                    self.player_name = player_name
                    self.dkp_spent = player_loot_entry[4][2]
                    self.readable_date = timestamp_to_datetime(player_loot_entry[1])

        else:
            raise ValueError(f"Points spent were not found for player {player_name}")
        
    def __str__(self):
        return (f"**Item:** {self.link_item}\n"
                f"**Player:** {self.player_name}\n"
                f"**DKP spent:** {self.dkp_spent}\n"
                f"**Time:** {self.readable_date}\n")