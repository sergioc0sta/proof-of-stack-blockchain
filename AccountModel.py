class AccountModel():
    def __init__(self) -> None:
        self.accounts = []
        self.balance = {}
        
    def addAcount(self, publicKey) -> None:
        if not publicKey in self.accounts:
            self.accounts.append(publicKey)
            self.balance[publicKey] = 0

    def addBalance(self, publicKey) -> dict:
        if publicKey not in self.balance:
            self.addAcount(publicKey)
        return self.balance[publicKey]
    
    def updateBalance(self, publicKey, amount) -> None:
        if publicKey not in self.balance:
            self.addAcount(publicKey)
        self.balance[publicKey] += amount