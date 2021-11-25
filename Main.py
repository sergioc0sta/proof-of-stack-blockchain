from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    transaction = wallet.createTransaction(receiver, amount, type)

    signatureValid = wallet.signatureValidation(transaction.payload(), transaction.signature, wallet.publicKeyString())
    
    print(signatureValid)