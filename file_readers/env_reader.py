import os
from dotenv import load_dotenv
from exceptions.env_reader_error import ConfigEnvironmentError, EnvFileNotFound, EnvVarMissingError

class EnvReader:
        
    def __init__(self):
        self._load_env_data()
    
    def get_discord_token(self):
        token = os.getenv("TOKEN")
        if not token:
            raise EnvVarMissingError("TOKEN")

        return token
    
    def get_logs_path(self):
        raid_logs_path = os.getenv("LOGS_PATH")
        if not raid_logs_path:
            raise EnvVarMissingError("LOGS_PATH")
        
        return raid_logs_path



    def _load_env_data(self):
        
        # Retrieves the Discord token from the .env file, ensuring the environment variable is set
        dotenv_path = os.getenv("DKPBOT_CONFIG_PATH")
        if not dotenv_path:
            raise ConfigEnvironmentError()

        if not os.path.exists(dotenv_path):
            raise EnvFileNotFound()
        
        load_dotenv(dotenv_path, override = True)
