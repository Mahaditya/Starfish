from .Block import Block

class Code(Block):
    def __init__(self,inner_code):
        self.inner_code=inner_code
    def create(self):
        return self.language.headers(self.inner_code)
    