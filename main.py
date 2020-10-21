from Function import Function as function
from Loop import For as loop
from Class import Class 
from out import export
from LanguageFactory import LanguageFactory as lf
from Block import Block
from Code import Code

language=lf.select_language('cpp')
Block.language=language
read=language.read
read_array=language.read_array
declare = language.declare
print_out=language.print_out
call= language.call

code=Code([
    function('Solution','int',[
        declare('M','int'),
        read('N','int'),
    ]),
    function('main','int',[
        declare('N','int'),
        loop('0','N',1,[
            read('N','int'),
            read_array('N','10','int')
        ]),
        print_out(call('Solution')),

    ]),
])

print(code)

