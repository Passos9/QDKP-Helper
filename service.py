from utils.converters import timestamp_to_date
from datetime import datetime
from model.player_dkp import PlayerDKP
from model.player_item import PlayerItem
from container.player_dkp_container import PlayerDkpContainer
from container.player_item_container import PlayerItemContainer
from file_readers.json_reader import JsonReader
from file_readers.env_reader import EnvReader
from file_readers.lua_reader import LuaFileReader
from exceptions.file_reader_error import FileReaderError
from exceptions.validation_error import RaidNameNotRecognized, EmptyDKPlist, EmptyPlayerItemlist, InvalidRaidDate
import os


class Service:
    def __init__(self):
        self.lua = LuaFileReader()
       
    def get_player_dkp(self):

        try:
            env_reader = EnvReader()
            json_reader = JsonReader()
            logs_path = env_reader.get_logs_path()
            server, guild = json_reader.get_server_and_guild()
            ignore_list = json_reader.get_ignore_list()
            guild_notes = self.lua.get_guild_notes(logs_path, server, guild)

        except FileReaderError as e:
            return str(e)
        
        timestamp = os.path.getmtime(logs_path)
        dkp_date = timestamp_to_date(timestamp)

        player_dkp_container = PlayerDkpContainer(dkp_date, ignore_list)

        for player, dkp_data in guild_notes.items():  
            try:
                total, total_spent = dkp_data 
                playerDKP = PlayerDKP(player, total, total_spent)  
                print(playerDKP)
                player_dkp_container.add(playerDKP)
            except ValueError:
                continue

        try:
            player_dkp_container.validate()
        except EmptyDKPlist as e:
            return str(e)
        
        return player_dkp_container
    

    def get_player_loot(self, raid, date):
        try:
            
            json_reader = JsonReader()
            env_reader = EnvReader()

            try:
                raid_name = self._raid_selector(raid, json_reader)
            except RaidNameNotRecognized as e:
                return str(e)
            
            logs_path = env_reader.get_logs_path()
            dkp_master, server, guild = json_reader.get_dkp_master_info()

            if date is None:
                timestamp, players_loot = self.lua.get_raid_loot(raid_name, None, logs_path, dkp_master, server, guild)
                raid_date = timestamp_to_date(timestamp)
            else:
                try:
                    raid_date = datetime.strptime(date, "%Y-%m-%d").date()
                    print(f"Raid date: {raid_date}")
                except ValueError:
                    return str(InvalidRaidDate(date))
        
                players_loot = self.lua.get_raid_loot(raid_name, raid_date, logs_path, dkp_master, server, guild)     
        
            wow_data_url = json_reader.get_wow_data_URL()

        except FileReaderError as e:
            return str(e)


        player_item_container = PlayerItemContainer(raid_name, raid_date)

        for player_name in players_loot.keys():
            player_loot_logs = players_loot[player_name]
            
            for i in range(len(player_loot_logs)):
                try:
                    player_item = PlayerItem(player_name, player_loot_logs[i], wow_data_url)
                except ValueError as e:
                    print(f"Entry {i}: {e}")
                    continue

                player_item_container.add(player_item)

        try:
            player_item_container.validate()
        except EmptyPlayerItemlist as e:
            return str(e)
        

        return player_item_container
    

    def _raid_selector(self, raid, json_reader):
        icc25_session_name = json_reader.get_icc25_session_name()
        rs25_session_name = json_reader.get_rs25_session_name()

        match raid:
            case "icc25":
                return icc25_session_name
            case "rs25":
                return rs25_session_name
            case _:
                raise RaidNameNotRecognized(raid)
        