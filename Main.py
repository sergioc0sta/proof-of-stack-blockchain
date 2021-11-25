from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet

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
        
    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)
    
    print(pool.transactions)
        

    #signatureValid = wallet.signatureValidation(transaction.payload(), transaction.signature, wallet.publicKeyString())
    #print(signatureValid)