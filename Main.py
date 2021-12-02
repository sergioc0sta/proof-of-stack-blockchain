from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
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
          
    blockchain = Blockchain()
    
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].paylaod()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)
    
    if not blockchain.blockCountValidate(block):
        print("Invalid Count")
        
    if not blockchain.blockHashValidate(block):
        print("Invalid Hash")
      
    if blockchain.blockCountValidate(block) and blockchain.blockHashValidate(block):
        blockchain.addBlock(block)
        print("New block added")
    
    signatureValidations = wallet.signatureValidation(block.paylaod(), block.signature, wallet.publicKeyString())
    