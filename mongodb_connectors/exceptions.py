class InvalidURIError(Exception):
    """Raised when a MongoDB URI is invalid"""
    pass

class URINotFoundError(Exception):
    """Raised when a requested URI doesn't exist"""
    pass
