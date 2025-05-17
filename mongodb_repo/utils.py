from .uris import MONGO_URIS
from .exceptions import MongoUriNotFoundError

def get_mongo_uri(key: str) -> str:
    if key not in MONGO_URIS:
        raise MongoUriNotFoundError(f"No MongoDB URI found with key '{key}'")
    return MONGO_URIS[key]

def list_all_uris() -> dict:
    return MONGO_URIS.copy()
