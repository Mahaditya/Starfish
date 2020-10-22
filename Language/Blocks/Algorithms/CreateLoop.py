from .Algorithm import Algorithm

class CreateLoop(Algorithm):

    def __init__(self,start,end,step,inner_code):
        self.start=start
        self.end=end
        self.step=step
        self.inner_code=inner_code

    def python3(self):
        return f'for i in range({self.start},{self.end},{self.step}):{self.inner_code}'
    
    def python2(self):
        return f'for i in range({self.start},{self.end},{self.step}):{self.inner_code}'

    def cpp(self):
        return f'for(int i={self.start},i<{self.end},{"i++" if self.step=="1" else "i=i+"+self.step}){{{self.inner_code}}}'

    def php(self):
        return f'for($i={self.start},$i<{self.end},i+={self.step}){{{self.inner_code}}}'


