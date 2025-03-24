class FileReaderError(Exception):
    """Base class for all custom Reader exceptions."""
    
    def __init__(self, message=None):
        if message is None:
            message = "An application error occurred."
        super().__init__(message)