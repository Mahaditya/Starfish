from abc import ABC, abstractmethod

class Language(ABC):

    '''Abstract Methods Mandatory for all Languages'''

    @abstractmethod
    def loop(self):
        pass
    @abstractmethod
    def function(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def read_array(self):
        pass
    @abstractmethod
    def call(self):
        pass
    @abstractmethod
    def print_out(self):
        pass


    ''' Optional Methods'''

    def declare(self,name,vartype,container='var'):
        return "not_supported"
    def declare_array(self,name,vartype,container='var'):
        return "not_supported"
    def headers(self,code):
        return code
    def create_class(self,name,inner_code,access_specifier):
        return "not_supported"











