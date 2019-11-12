import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #Creates new Block & adds it to the chain
        pass

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
                'recipient': recipiet,
                'amount': amount
            })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #to hash blocks
        pass

    @property
    def last_block(self):
        #returns last block of a chain
        pass

print('run blockchain\n')