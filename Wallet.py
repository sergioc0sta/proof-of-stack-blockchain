from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils

class Wallet():
    
    def __init__(self) -> None:
        self.keyPair = RSA.generate(2048)
        
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureObject.sign(dataHash)
        return signature.hex()
    
    @staticmethod
    def signatureValidation(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publiKey = RSA.importKey(publicKeyString)
        signatureSchemaObject = PKCS1_v1_5.new(publiKey)
        signatureValidation = signatureSchemaObject.verify(dataHash, signature)
        return signatureValidation
    
    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString
        