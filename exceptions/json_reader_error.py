from exceptions.file_reader_error import FileReaderError

class JsonFileNotFoundError(FileReaderError):
    def __init__(self):
        super().__init__("config.json file not found. Please make sure the file is in the source code directory")

class JsonRunTimeError(FileReaderError):
    def __init__(self):
        super().__init__("There was an issue opening the config.json file. Please check the setup and try again")

class JsonFilePermissionError(FileReaderError):
    def __init__(self):
        super().__init__("Permission denied when trying to access the config.json file. Please check the file permissions and try again")

class JsonFileDecodeError(FileReaderError):
    def __init__(self):
        super().__init__("Permission denied when trying to access the config.json file. Please check the file permissions and try again")

class JsonFileIOError(FileReaderError):
    def __init__(self):
        super().__init__("The config.json file is not in a valid JSON format. Please ensure the file is properly formatted and try again")

class JsonFileInvalidError(FileReaderError):
    def __init__(self):
        super().__init__("There was an issue reading the config.json file. This could be due to a file system error. Please ensure the file is accessible and try again")

class JsonKeyError(FileReaderError):
    def __init__(self, key1):
        super().__init__(f"Missing key '{key1}' in the config.json file")

class JsonTypeError(FileReaderError):
    def __init__(self):
        super().__init__("There was an error with the data type in the config.json file. Please ensure the file is formatted correctly")

class JsonDataRunTimeError(FileReaderError):
    def __init__(self):
        super().__init__("There was an issue reading the config.json file. Please check the setup and try again.")