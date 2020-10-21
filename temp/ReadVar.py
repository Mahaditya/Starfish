from Algorithm import Algorithm
class ReadVar(Algorithm):
    def __init__(self,name,vartype):
        self.name=name
        self.vartype=vartype

    def python3(self):
        if self.vartype=='int':
            return f'{self.name}=int(input())'




