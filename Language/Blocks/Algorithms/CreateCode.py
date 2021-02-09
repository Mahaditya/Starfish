from .Algorithm import Algorithm
from .Strings import javascriptHeader 
class CreateCode(Algorithm):

    def __init__(self,inner_code):
        self.inner_code=inner_code

    def cpp(self):
        return f'#include<bits/stdc++.h>\nusing namepace std;\n{self.inner_code}'
    
    def php(self):
        return f' <?php \n {self.inner_code} ?> '

    def python3(self):
        return self.inner_code

    def python2(self):
        return self.inner_code

    def java(self):
        return f'import java.io.*;\nimport java.util.*;\npublic class  Result{{\n{self.inner_code}}}'

    def golang(self):
        return f'package main\nimport(\n "fmt"\n) \n{self.inner_code}'
    
    def javascript(self):
        return javascriptHeader.header+f'\n{self.inner_code}'
    
    def csharp(self):
        return f'using System;\nusing System.Linq;\npublic class  Result{{\n{self.inner_code}}}'

    def C(self):
        return f'#include<stdio.h>\n{self.inner_code}'
    
    def ruby(self):
        return self.inner_code