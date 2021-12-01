from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
import pprint
if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    pool = TransactionPool()
    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)
          
    block = wallet.createBlock(pool.transactions, 'lastHash', 1)
    pprint.pprint(block.toJson())
    
    signatureValidations = wallet.signatureValidation(block.paylaod(), block.signature, wallet.publicKeyString())
    print(signatureValidations)