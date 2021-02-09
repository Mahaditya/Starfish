class Algorithm:
    language="python3"
    data_types={
        "int":{
            "python3":"int",
            "python2":"int",
            "java":"int",
            "cpp":"int",
            "php":"int",
            "csharp":"int",
            "ruby":"int",
            "golang":"int",
            "javascript":"int",
            "C":"int",
            "ruby":"int",
        },
        "long":{
            "cpp":"long",
            "golang":"int64",
            "java":"long",
            "csharp":"long",
        },
        "char":{
            "cpp":"char",
        },
        "void":{
            "cpp":"void",
            "java":"void",
            "csharp":"void",
            "golang":"",
            "php":"void",
            "python3":"void",
            "python2":"void",
        }

    }
    # def get_type(self,vartype):
    #     return self.data_types[vartype][self.language]

    def python3(self):
        return "not_implemented"
    def cpp(self):
        return "not_implemented"
    def php(self):
        return "not_implemented"
    def python2(self):
        return "not_implemented"
    def java(self):
        return "not_implemented"
    def csharp(self):
        return "not_implemented"
    def golang(self):
        return "not_implemented"
    def javascript(self):
        return "not_implemented"
    def C(self):
        return "not_implemented"
    def ruby(self):
        return "not_implemented"

    def languageMethods(self,language):
        return_string={
            "python3":self.python3(),
            "cpp":self.cpp(),
            "php":self.php(),
            "python2":self.python2(),
            "java":self.java(),
            "csharp":self.csharp(),
            'golang':self.golang(),
            "javascript":self.javascript(),
            "C":self.C(),
            "ruby":self.ruby(),
        }
        return return_string[language]

    def create(self):
        return self.languageMethods(self.language)



