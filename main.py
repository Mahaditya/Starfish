from Language.Selector import select_language
from Language.Blocks.Algorithms.ReadVar import ReadVar
from Language.Blocks.Function import Function as function
from Language.Blocks.Code import Code
from Language.Blocks.Loop import For as loop
# from Language.Blocks.Algorithms.ReadArray import ReadArray
select_language("python3")

code=Code([

function("solution","void",[
    ReadVar("count","int"),
    loop('1','N','1',[
        ReadVar("count","int"),
        ReadVar("N","int"),
    ])
]),

function("main","void",[
    ReadVar("count","int"),
    loop('1','N','1',[
        ReadVar("count","int"),
    ])
])

])

print(code)