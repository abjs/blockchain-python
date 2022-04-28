from helpers.hash import hash_data


def hash_user_data(data):
    """
    Returns the encrypted data.
    """
    details = {
        "aadharaNumber": data['aadharaNumber'],
    }
    hash = hash_data(details)
    vote = data['vote']
    return hash, vote
