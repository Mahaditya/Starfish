from .Algorithm import Algorithm
class ReadVar(Algorithm):
    def __init__(self,name,vartype):
        self.name=name
        self.vartype=vartype

    def python3(self):
        if self.vartype=='int':
            return f'{self.name}=int(input())'

    def python2(self):
        if self.vartype=='int':
            return f'{self.name}=input()'

    def cpp(self):
        if self.vartype=='int':
            return f'cin>>{self.name};'

    def php(self):
        if self.vartype=='int':
            return f'${self.name} = (int)trim(fgets(STDIN));'

    def java(self):
        if self.vartype=='int':
            return f'{self.name} = Integer.parseInt(br.readLine())'

    def javascript(self):
        if self.vartype=='int':
            return f'let {self.name} = readLine()'
    
    def csharp(self):
        if self.vartype=='int':
            return f'{self.name} = Convert.ToInt32(Console.ReadLine());'
 
    def C(self):
        if self.vartype=='int':
            return f'scanf("%d",&{self.name});'
    
    def ruby(self):
        if self.vartype=='int':
            return f'{self.name}=gets.chomp.to_i'


