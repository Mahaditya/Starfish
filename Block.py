from LanguageFactory import LanguageFactory as lf
from abc import ABC, abstractmethod


class Block(ABC):
    language=lf.select_language('python3')
    def __repr__(self):
        return self.compile(self,self)

    @staticmethod
    def compile(self,code_block,depth=1):
        statements=""
        spacing = '\t'*depth
        for statement in code_block.inner_code:
            if statement=="not_supported" :
                continue
            elif isinstance(statement,Block):
                statements=statements+'\n'+spacing+self.compile(self,statement,depth+1)
            else:
                statements=statements+'\n'+spacing+statement
        code_block.inner_code=statements
        return code_block.create()

    @abstractmethod
    def create(self):
        pass