from .uris import URI_DATABASE
from .exceptions import InvalidURIError, URINotFoundError
from pymongo import MongoClient
from urllib.parse import urlparse

def validate_uri(uri: str) -> bool:
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_uri(connection_name: str) -> str:
    if connection_name not in URI_DATABASE:
        raise URINotFoundError(f"No URI found for connection '{connection_name}'")
    return URI_DATABASE[connection_name]

def list_uris() -> dict:
    return URI_DATABASE.copy()

def add_uri(connection_name: str, uri: str, overwrite=False):
    if not validate_uri(uri):
        raise InvalidURIError(f"Invalid MongoDB URI format: {uri}")
    if connection_name in URI_DATABASE and not overwrite:
        raise KeyError(f"Connection '{connection_name}' already exists")
    URI_DATABASE[connection_name] = uri
