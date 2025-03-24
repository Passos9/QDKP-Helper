from exceptions.file_reader_error import FileReaderError

class LuaFileNotFoundError(FileReaderError):
    def __init__(self):
        super().__init__("Lua file not found. Please make sure the path to QDKP_V2.lua is correctly set on .env file")

class LuaIsADirectoryError(FileReaderError):
    def __init__(self):
        super().__init__("The path set to QDKP_V2.lua on .env file is a directory, not a file")

class LuaPermissionError(FileReaderError):
    def __init__(self):
        super().__init__("Permission denied opening QDKP_V2.lua. Please check file permissions")

class LuaFileUnreadableError(FileReaderError):
    def __init__(self):
        super().__init__("Unreadable Lua file (QDKP_V2.lua): Invalid characters or encoding issue")

class LuaFileOSError(FileReaderError):
    def __init__(self):
        super().__init__("Error: An OS error occurred while trying to read the file QDKP_V2.lua. Please try again")

class LuaRaidNotFound(FileReaderError):
    def __init__(self, raid):
        super().__init__(f"No raid named {raid} was found. Please make sure to start dkp session at the start of every raid and that config.json has the correct server, guild and dkp master")

class LuaRaidDateNotFound(FileReaderError):
    def __init__(self, raid, date):
        super().__init__(f"The raid '{raid}' was not found for {date}. Ensure the raid took place on this date and that the addon's storage settings retain enough entries")







