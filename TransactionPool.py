class TransactionPool():
    def __init__(self) -> None:
        self.transactions = []
        
    def addTransaction(self, transaction) -> list:
        self.transactions.append(transaction)
        
    def transactionExists(self, transaction) -> bool:
        for withTransaction in self.transactions:
            if withTransaction.isTheSameTransaction(transaction):
                return True
        return False