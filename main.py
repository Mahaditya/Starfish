from Language.Selector import select_language
from Language.Blocks.Algorithms.ReadVar import ReadVar
from Language.Blocks.Function import Function as function
from Language.Blocks.Loop import For as loop
select_language("cpp")

func=function("main","int",[
    ReadVar("count","int"),
    loop('1','N','1',[
        ReadVar("count","int"),
        ReadVar("N","int"),
    ])
])

print(func)