from abc import ABC, abstractmethod

class Block(ABC):
    language='python3'
    block_start="{"
    block_end="}"

    block_starts={
            "python3":":",
            "cpp":"{",
            "php":"{",
            "python2":":",
            "java":"{",
            "csharp":"{",
            'golang':"{",
            "javascript":"{",
            "C":"{",
            "ruby":"",
    }

    block_ends={
            "python3":"",
            "cpp":"}",
            "php":"}",
            "python2":"",
            "java":"}",
            "csharp":"}",
            'golang':"}",
            "javascript":"}",
            "C":"}",
            "ruby":"end",
    }

    def __repr__(self):
        return self.compile(self,self)

    @staticmethod
    def compile(self,code_block,depth=0):
        statements=""
        spacing = '\t'*depth
        for statement in code_block.inner_code:
            if isinstance(statement,Block):
                statements=statements+'\n'+spacing+self.compile(self,statement,depth+1)
            elif statement.create()=="not_implemented" :
                continue
            else:
                statements=statements+'\n'+spacing+statement.create()
        if depth==0:
            code_block.inner_code=statements 
        else: 
            code_block.inner_code = self.block_starts[self.language]+f'{statements}'+'\n'+'\t'*(depth-1)+self.block_ends[self.language]
        return code_block.create()

    @abstractmethod
    def create(self):
        pass