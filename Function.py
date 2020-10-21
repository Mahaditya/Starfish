from Block import Block

class Function(Block):
    def __init__(self,name,return_type,inner_code):
        self.name=name
        self.return_type=return_type
        self.inner_code=inner_code
    def create(self):
        return self.language.function(self.name,self.return_type,self.inner_code)



        


