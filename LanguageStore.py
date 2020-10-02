from Language import Language

class Python3(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f'{name} = list(map(int, input().split()))'
    def read(self,name,vartype):
        if vartype=='int':
            return f'{name}=int(input())'
    def function(self,name,return_type,inner_code):
        return f'''def {name}():\n\t{inner_code}'''
    def loop(self,start,end,step,inner_code):
        return f'for i in range({start},{end},{step}):\n\t{inner_code}'
    def create_class(self,name,inner_code,access_specifier):
        return f'class {name}:\n\t{inner_code}'

class Python2(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f'{name} = list(map(int, raw_input().split()))'
    def read(self,name,vartype):
        if vartype=='int':
            return f'{name}=input()'
    def function(self,name,return_type,inner_code):
        return f'''def {name}():\n\t{inner_code}'''
    def loop(self,start,end,step,inner_code):
        return f'for i in range({start},{end},{step}):\n\t{inner_code}'

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
        return f'function {name}(){{\n{inner_code}\n}}'
    def loop(self,start,end,step,inner_code):
        return f'for($i={start},$i<{end},i+={step}){{\n\t{inner_code}}}'

class CPP(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f'''for(int i=0;i<{count};i++){{cin>>{name}[i];}}'''
    def read(self,name,vartype):
        if vartype=='int':
            return f'cin>>{name};'
    def headers(self,code):
        return f'#include<bits/stdc++.h>\nusing namepace std;\n{code}'
    def function(self,name,return_type,inner_code):
        return f'''{return_type} {name}(){{\n{inner_code}}}'''
    def loop(self,start,end,step,inner_code):
        return f'for(int i={start},i<{end},i=i+{step}){{\n{inner_code}}}'
    def declare(self,name,vartype,container='var'):
        if vartype=='int' and container=='var':
            return f'{vartype} {name};'
        elif vartype=='string' and container=='var':
            return f'{vartype} {name};'
        elif vartype=='int' and container=='array':
            return f'vector<{vartype}>{name};'



