from .Block import Block
from .Algorithms.CreateCode import CreateCode

class Code(Block):
    def __init__(self,inner_code):
        self.inner_code=inner_code
    def create(self):
        return CreateCode(self.inner_code).create()
    
    