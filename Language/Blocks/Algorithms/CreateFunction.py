from .Algorithm import Algorithm

class CreateFunction(Algorithm):

    def __init__(self,name,return_type,inner_code):
        self.name=name
        self.return_type=return_type
        self.inner_code=inner_code

    def python3(self):
        return f'def {self.name}():{self.inner_code}'
    
    def python2(self):
        return f'def {self.name}():{self.inner_code}'

    def cpp(self):
        return f'{self.return_type} {self.name}(){{{self.inner_code}\n\t}}'

    def php(self):
        return f'function {self.name}(){{{self.inner_code}\n}}'
