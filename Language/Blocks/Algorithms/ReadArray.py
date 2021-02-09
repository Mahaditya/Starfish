from .Algorithm import Algorithm

class ReadArray(Algorithm):

    def __init__(self,name,count,vartype):
        self.name=name
        self.count=count
        self.vartype=self.data_types[vartype][self.language]

    def python3(self):
        if self.vartype=='int':
            return f'{self.name} = list(map(int, input().split()))'
    def cpp(self):
        if self.vartype=='int':
            return f'for(int i=0;i<{self.count};i++){{cin>>{self.name}[i];}}'
    def php(self):
        if self.vartype=='int':
            return f"${self.name} = array_map('intval',explode(" ", trim(fgets(STDIN))));"
    def python2(self):
        if self.vartype=='int':
            return f'{self.name} = list(map(int, raw_input().split()))'

