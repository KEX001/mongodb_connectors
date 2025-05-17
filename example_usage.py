from mongodb_connectors import get_uri, list_uris, add_uri
from pymongo import MongoClient

# Example 1: Basic Usage
primary_uri = get_uri('bikash_primary')
client = MongoClient(primary_uri)
print(f"Connected to: {client.server_info()['version']}")

# Example 2: List all connections
print("\nAvailable connections:")
for name, uri in list_uris().items():
    print(f"{name}: {uri[:25]}...")  # Show first 25 chars for security

# Example 3: Add new connection
try:
    add_uri('new_cluster', 'mongodb+srv://user:pass@new-cluster.example.net/')
    print("\nSuccessfully added new connection")
except Exception as e:
    print(f"\nFailed to add connection: {e}")
