from Block import Block

class Class(Block):
    def __init__(self,name,inner_code,access_specifier='public'):
        self.name=name
        self.access_specifier=access_specifier
        self.inner_code=inner_code
    def create(self):
        return self.language.create_class(self.name,self.inner_code,self.access_specifier)

