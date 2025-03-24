from exceptions.file_reader_error import FileReaderError

class ConfigEnvironmentError(FileReaderError):
    def __init__(self):
        super().__init__("DKPBOT_CONFIG_PATH is not set! Please configure it in your system")

class EnvFileNotFound(FileReaderError):
    def __init__(self):
        super().__init__(".env file not found in the directory specified by the DKPBOT_CONFIG_PATH environment variable. Please ensure the path is correct and the file exists")

class EnvVarMissingError(FileReaderError):
    def __init__(self, Var):
        super().__init__(f"{Var} is not set in the .env file. Please add it and try again")