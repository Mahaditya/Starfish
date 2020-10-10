
class PHP(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f"${name} = array_map('intval',explode(" ", trim(fgets(STDIN))));"
    def read(self,name,vartype):
        if vartype=='int':
            return f'${name} = (int)trim(fgets(STDIN));'
    def headers(self,code):
        return f''' <?php \n {code} ?> '''
    def function(self,name,return_type,inner_code):
        return f'function {name}(){{{inner_code}\n}}'
    def loop(self,start,end,step,inner_code):
        return f'for($i={start},$i<{end},i+={step}){{{inner_code}}}'
    def call(self,name):
        return f'{name}();'
    def print_out(self,obj):
        return f'echo {obj}'