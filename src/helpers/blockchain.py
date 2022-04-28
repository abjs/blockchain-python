from time import time

from helpers.hash import hash_data
from datetime import datetime

from helpers.user import hash_user_data


def get_hash(block):
    """
    Returns the hash of the block.
    """
    return block['hash']


def get_previous_block(blockchain):
    """
    Returns the previous block.
    """
    if get_blockchain_size(blockchain) >= 1:
        return blockchain[-1]
    else:
        return None


def get_block_data(block):
    """
    Returns the data of the block.
    """
    return block['data']


def get_block_timestamp(block):
    """
    Returns the timestamp of the block.
    """
    return block['timestamp']


def get_block_index(block):
    """
    Returns the index of the block.
    """
    return block['index']


def get_block_hash(block):
    """
    Returns the hash of the block.
    """
    return block['hash']


def get_previous_hash(block):
    """
    Returns the previous hash of the block.
    """
    return block['previous_hash']


def get_blockchain_size(blockchain):
    """
    Returns the size of the blockchain.
    """
    return len(blockchain)


def genarate_blockchain(blockchain):
    timestamp = str(datetime(2022, 1, 1, 12, 0, 0))
    block = {
        'index': 0,
        'previous_hash': "0",
        "user_hash": "0",
        'timestamp': timestamp,
    }
    block['hash'] = hash_data(block)
    blockchain.append(block)
    return blockchain


def check_chain_validity(blockchain):
    result = True
    for index in range(1, len(blockchain)):
        current_block = blockchain[index]
        previous_block = blockchain[index - 1]
        if current_block['hash'] != current_block['hash']:
            result = False
        if current_block['previous_hash'] != previous_block['hash']:
            result = False
    return result


def check_user_vote(blockchain, user_hash):
    for block in blockchain:
        if block['user_hash'] == user_hash:
            return block['vote']
    return None


def add_new_block(blockchain, data):
    previous_block = get_previous_block(blockchain)
    index = get_block_index(previous_block) + 1
    previous_hash = get_block_hash(previous_block)
    timestamp = str(datetime.now())
    user_hash, vote = hash_user_data(data)
    if check_user_vote(blockchain, user_hash) is None:
        block = {
            'index': index,
            'previous_hash': previous_hash,
            'timestamp': timestamp,
            'user_hash': user_hash,
            'vote': vote,
        }
        block['hash'] = hash_data(block)
        blockchain.append(block)
        return blockchain
    else:
        print("User already voted")
        return {"error": True, "message": "User already voted"}
