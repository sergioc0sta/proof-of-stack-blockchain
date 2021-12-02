import time
import copy

class Block():
    
    def __init__(self, transactions, lastHash, forger, blockCount) -> None:
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''
        
    @staticmethod
    def genesis():
        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timestamp = 0
        return genesisBlock
        
    def toJson(self) -> dict:
        data = {}
        data['lastHash'] = self.lastHash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] =self.timestamp
        data['signature'] = self.signature
        transactions = []
        for transaction in self.transactions:
            transactions.append(transaction.toJson())
        data['transactions'] = transactions
        return data
    
    def paylaod(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation
        
    def sign(self, signature):
        self.signature = signature