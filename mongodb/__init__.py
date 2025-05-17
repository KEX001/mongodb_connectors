"""
Usage:
    from mongodb import MONGO_URIS
    uri = MONGO_URIS.get('bikash_primary')
    
    or
    
    from mongodb_repo import get_mongo_uri
    uri = get_mongo_uri('bikash_primary')
"""

from .uris import MONGO_URIS
from .utils import get_mongo_uri, list_all_uris
from .exceptions import MongoUriNotFoundError

__all__ = ['MONGO_URIS', 'get_mongo_uri', 'list_all_uris', 'MongoUriNotFoundError']
__version__ = '1.0.0'
