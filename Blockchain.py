from Block import Block
from BlockchainUtils import BlockchainUtils

class Blockchain():
    
    def  __init__(self) -> None:
        self.blocks = [Block.genesis()]
        
    def addBlock(self, block) -> None:
        self.blocks.append(block)
        
    def toJson(self) -> dict:
        data = {}
        jsonBlock = []
        for blk in self.blocks:
            jsonBlock.append(blk.toJson())
        data['blocks'] = jsonBlock
        return data
    
    def blockCountValidate(self, block) -> bool:
        if self.blocks[-1].blockCount == block.blockCount -1:
            return True
        else:
            return False
    
    def blockHashValidate(self, block) -> bool:
        latestBlockchainHash = BlockchainUtils.hash(self.blocks[-1].paylaod()).hexdigest()
        if latestBlockchainHash == block.lastHash:
            return True
        else:
            return False