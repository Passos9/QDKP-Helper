import lupa
from utils.converters import timestamp_to_date
from exceptions.lua_reader_error import LuaFileNotFoundError, LuaIsADirectoryError, LuaPermissionError, LuaFileUnreadableError, LuaFileUnreadableError, LuaFileOSError, LuaRaidDateNotFound, LuaRaidNotFound
import logging


# This class has the purpose of converting Lua tables to Python lists or dictionaries
# Only the necessary information is retrieved, therefore it contains some filter logic
class LuaFileReader:
  def __init__(self):
    self.lua = lupa.LuaRuntime(unpack_returned_tuples=True)

  def get_guild_notes(self, logs_path, server, guild):

    lua_code = self.__open_lua_file(logs_path)

    self.lua.execute(lua_code)
    qdkp_data = self.lua.globals().QDKP2_Data
    guild_notes = qdkp_data[server + '-' + guild]['note']

    guild_notes_dict = {}

    for player, values in guild_notes.items():
        total = values[1]  
        total_spent = values[2]   

        # Add the calculated net and total_spent for the player
        guild_notes_dict[player] = [total, total_spent]

    return guild_notes_dict
  

  def get_raid_loot(self, raid_name, date, raid_logs_path, dkp_master, server, guild):

    lua_code = self.__open_lua_file(raid_logs_path)

    self.lua.execute(lua_code)
    qdkp_data = self.lua.globals().QDKP2_Data # qdkp_data references the lua table object
    logs = qdkp_data[server + '-' + guild]['log']

    raid = {}
    number_aux = 0
    readable_date = ""

    # Iterate over the Lua table keys (logs)
    for logskey in logs.keys():
        
        # In the future it, the raid itself could be made selectable in the discord command
        # For example logs[logskey]["_NAME"] == "raid_selected"
        if logskey.endswith(dkp_master) and logs[logskey]["_NAME"] == raid_name:
            
            raid = logs[logskey]

            # If date is provided
            if date is not None:
              timestamp = raid["_TSTA"] 
              readable_date = timestamp_to_date(timestamp)

              # Compares date inserted with raid's date: if matches it returns the raid_players logs
              if date == readable_date:
                raid_players = self.__get_raid_players(raid)
                return raid_players
            
            # If date is not provided it keeps track of the number
            # This is because the most recent raid is always the last one found
            else: 
              divided_key = logskey.split(".")
              number = int(divided_key[0])
              if number > number_aux:
                number_aux = number
    
    # If date is None it retrieves the most recent raid_players logs (last ICC raid found)
    if date is None:
        number_str = str(number_aux)
        raid = logs[number_str + "." + dkp_master]
        if raid is None:
          raise LuaRaidNotFound(raid_name)
        else:   
          timestamp = raid["_TSTA"] 
          raid_players = self.__get_raid_players(raid)
          return timestamp, raid_players
       
    # If it didn't find any raid in which the date inserted is equal to 
    if date is not None:
      raise LuaRaidDateNotFound(raid_name, date)
        


  def __get_raid_players(self, raid):

    raid_players = {}

    for key in raid.keys():
        #Filtering for players
        if not (key.startswith('_') or key == 'RAID'): # Then the key is a player
            raid_player = raid[key]
            # Convert all Lua tables in raid_player to Python equivalents
            items_bought_logs = []
            
            for i in range(1, len(raid_player) + 1): # Converted Lua table expects 1-based indexing
              # Filtering for points gathered and spent
              item_bought_logs = []
              for j in range(1, len(raid_player[i]) + 1):
                  value = raid_player[i][j]
                  #print(f"Value of raid_player{[i]}{[j]}: {value}\n")
                  if j == 5:
                      converted_value = self.__convert_lua_value(value)
                      #print(f"Converted value for i={i}, j={j}: {converted_value}")  # Debugging output
                  else:
                      converted_value = value

                  item_bought_logs.append(converted_value)
              
              if len(item_bought_logs) == 5: # Only the take the entries that have both the item and the points spent
                items_bought_logs.append(item_bought_logs)

            raid_players[key] = items_bought_logs # Every item bought for this specific player (key)

    return(raid_players)
  
    
  def __convert_lua_value(self, value):     
      key = next(iter(value))
      single_value = value[key]
      return {key: single_value} #returns a python dictionary
        
    
  def __open_lua_file(self, path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise LuaFileNotFoundError()
    except IsADirectoryError:
        raise LuaIsADirectoryError()
    except PermissionError:
        raise LuaPermissionError()
    except UnicodeDecodeError:
        raise LuaFileUnreadableError()
    except OSError as e:
        logging.error(f"Error: An OS error occurred while trying to read the QDKP_V2.lua. Details: {e}", exc_info=True)
        raise LuaFileOSError()
    


        
    



    