from .Block import Block
from .Algorithms.CreateLoop import CreateLoop
class For(Block):
    def __init__(self,start,end,step,inner_code):
        self.start=start
        self.end=end
        self.step=step
        self.inner_code=inner_code
    def create(self):
        return CreateLoop(self.start,self.end,self.step,self.inner_code).create()