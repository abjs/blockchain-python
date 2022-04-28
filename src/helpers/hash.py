import hashlib


def hash_data(data):
    data = str(data).encode('utf-8')
    """
    Returns a sha256 hash of the data.
    """
    return hashlib.sha256(data).hexdigest()
