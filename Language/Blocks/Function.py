from .Block import Block
from .Algorithms.CreateFunction import CreateFunction
class Function(Block):
    def __init__(self,name,return_type,inner_code):
        self.name=name
        self.return_type=return_type
        self.inner_code=inner_code
    def create(self):
        return CreateFunction(self.name,self.return_type,self.inner_code).create()



        


