
class CPP(Language):
    def read_array(self,name,count,vartype='string'):
        if vartype=='int':
            return f'for(int i=0;i<{count};i++){{cin>>{name}[i];}}'
    def read(self,name,vartype):
        if vartype=='int':
            return f'cin>>{name};'
    def headers(self,code):
        return f'#include<bits/stdc++.h>\nusing namepace std;\n{code}'
    def function(self,name,return_type,inner_code):
        return f'''{return_type} {name}(){{{inner_code}\n\t}}'''
    def loop(self,start,end,step,inner_code):
        return f'for(int i={start},i<{end},i=i+{step}){{{inner_code}}}'
    def declare(self,name,vartype,container='var'):
        if vartype=='int' and container=='var':
            return f'{vartype} {name};'
        elif vartype=='string' and container=='var':
            return f'{vartype} {name};'
        elif vartype=='int' and container=='array':
            return f'vector<{vartype}>{name};'
    def call(self,name):
        return f'{name}();'
    def print_out(self,obj):
        return f'cout<<{obj}'
