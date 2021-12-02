from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from AccountModel import AccountModel
import pprint

if __name__ == '__main__':
    wallet = Wallet()
    accountModel = AccountModel()
    accountModel.addAcount(wallet.publicKeyString())
    
    accountModel.updateBalance(wallet.publicKeyString(), 20)
    accountModel.updateBalance(wallet.publicKeyString(), -3)
    
    print(accountModel.balance[wallet.publicKeyString()])