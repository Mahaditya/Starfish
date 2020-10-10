
class Python2(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f'{name} = list(map(int, raw_input().split()))'
    def read(self,name,vartype):
        if vartype=='int':
            return f'{name}=input()'
    def function(self,name,return_type,inner_code):
        return f'''def {name}():{inner_code}'''
    def loop(self,start,end,step,inner_code):
        return f'for i in range({start},{end},{step}):{inner_code}'
    def call(self,name):
        return f'{name}()'
    def print_out(self,obj):
        return f'print {obj}'