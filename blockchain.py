class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #Creates new Block & adds it to the chain
        pass

    @staticmethod
    def hash(block):
        #to hash blocks
        pass

    @property
    def last_block(self):
        #returns last block of a chain
        pass