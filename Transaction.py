import uuid
import time

class Transaction():
    def __init__(self, sendThePublicKey, receiverThePublicKey, amout, type) -> None:
        self.sensendThePublicKey = sendThePublicKey
        self.receiverThePublicKey = receiverThePublicKey
        self.amount = amout
        self.type = type
        self.id =uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def to_json(self) -> dict:
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature