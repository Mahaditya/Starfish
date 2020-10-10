from Block import Block

class For(Block):
    def __init__(self,start,end,step,inner_code):
        self.start=start
        self.end=end
        self.step=step
        self.inner_code=inner_code
    def create(self):
        return self.language.loop(self.start,self.end,self.step,self.inner_code)