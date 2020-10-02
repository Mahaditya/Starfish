from Function import Function as function
from Loop import For as loop
from Class import Class 
from out import export
from select_language import select_language
from Block import Block
from Code import Code
language=select_language('python3')
Block.language=language
read=language.read
read_array=language.read_array
declare = language.declare

code=Code([
    function('Solution','int',[
        declare('M','int')
    ]),
    function('main','int',[
        declare('N','int'),
        loop('0','N',1,[
            read('N','int')
        ])
    ]),
    Class('Soluton',[
        read('K','int')
    ])

])

print(code)

