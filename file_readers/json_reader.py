import json
import os
import logging
import sys
from exceptions.json_reader_error import JsonFileNotFoundError, JsonKeyError, JsonTypeError, JsonDataRunTimeError, JsonFilePermissionError, JsonFileDecodeError, JsonFileIOError, JsonRunTimeError

class JsonReader:

    def __init__(self):
        self.config_data = self._load_json_config()

    def get_command_prefix(self):
        return self._get_data("PREFIX")
    
    def get_server_and_guild(self):
        server = self._get_data("SERVER")
        guild = self._get_data("GUILD")

        return server, guild

    def get_dkp_master_info(self):
        dkp_master = self._get_data("DKP_MASTER")
        server = self._get_data("SERVER")
        guild = self._get_data("GUILD")

        return dkp_master, server, guild

    def get_icc25_session_name(self):
        return self._get_data("ICC25_SESSION_NAME")
    
    def get_rs25_session_name(self):
        return self._get_data("RS25_SESSION_NAME")
        
    def get_wow_data_URL(self):
        return self._get_data("WOW_DATA")

    def get_ignore_list(self):
        return self._get_data("IGNORE_LIST")


    def _load_json_config(self):
        config_path = self._get_config_path()
    
        if not os.path.exists(config_path):
            raise JsonFileNotFoundError()

        try:
            with open(config_path, 'r') as config_file:
                return json.load(config_file)
        except PermissionError:
            raise JsonFilePermissionError() 
        except json.JSONDecodeError:
            raise JsonFileDecodeError() 
        except IOError:
            raise JsonFileIOError()  
        except Exception as e:
            logging.error(f"Unexpected error: {e}", exc_info=True)
            raise JsonRunTimeError()
        
    def _get_config_path(self):
        # If running as an executable (PyInstaller)
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)  # Folder of bot.exe
        else:
            base_path = os.path.dirname(__file__)  # Folder of bot.py

        return os.path.join(base_path, "..", "config.json")


    def _get_data(self, key1):
        try:
            return self.config_data[key1]
        except KeyError:
            raise JsonKeyError(key1)
        except TypeError:
            raise JsonTypeError()
        except Exception as e:
            logging.error(f"Unexpected error: {e}", exc_info=True)
            raise JsonDataRunTimeError()
