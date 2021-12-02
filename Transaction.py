import uuid
import time
import copy

class Transaction():
    def __init__(self, sendThePublicKey, receiverThePublicKey, amout, type) -> None:
        self.sensendThePublicKey = sendThePublicKey
        self.receiverThePublicKey = receiverThePublicKey
        self.amount = amout
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self) -> dict:
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature
        
    def payload(self) -> dict:
        copyObject = copy.deepcopy(self.toJson())
        copyObject['signature'] = ''
        return copyObject
        
    def isTheSameTransaction(self, transaction) -> bool:
        if self.id == transaction.id:
            return True
        else:
            return False
        