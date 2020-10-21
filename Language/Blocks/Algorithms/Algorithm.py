class Algorithm:
    language="python3"
    data_types={
        "int":{
            "python3":"int",
            "cpp":"int"
        },
        "long":{
            "cpp":"long",
            "golang":"int64",
        },  
    }

    def python3(self):
        return "not_implemented"
    def cpp(self):
        return "not_implemented"
    def php(self):
        return "not_implemented"
    def python2(self):
        return "not_implemented"


    def languageMethods(self,language):
        return_string={
            "python3":self.python3(),
            "cpp":self.cpp(),
            "php":self.php(),
            "python2":self.python2(),
        }
        return return_string[language]

    def create(self):
        return self.languageMethods(self.language)



