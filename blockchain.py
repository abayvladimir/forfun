import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #create the genesis block
        self.new_block(previous_hash = 1, proof = 100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates new Block & adds it to the chain

        :param proof: <int> proof get from 
        :param previous_hash: (optional) <str> Hash of prev block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #reset current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates new transaction to go to the next block
        :param sender: <str> sender address
        :param recipient: <str> recipient address
        :param amount: <int> amount
        :return: <int> block index, that saves transaction data
        """
        self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 block hash

        :param block: <dict> Block
        :return: <str>
        """

        #We have to be sure that our Dict is corted
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
print('run blockchain\n')