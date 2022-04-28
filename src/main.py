import imp
import json
from helpers.blockchain import add_new_block, check_chain_validity, genarate_blockchain, get_previous_block
import json
if __name__ == '__main__':
    blockchain = []
    genarate_blockchain(blockchain)
    user = {
        "aadharaNumber": "123456789",
        "vote": "Yes"
    }
    add_new_block(blockchain, user)
    user = {
        "aadharaNumber": "1234567892",
        "vote": "No"
    }
    add_new_block(blockchain, user)
    user = {
        "aadharaNumber": "1234567892",
        "vote": "No"
    }
    add_new_block(blockchain, user)
    print(json.dumps(blockchain, indent=4))
    print(f"chain_validity {check_chain_validity(blockchain)}")
