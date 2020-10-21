import LanguageStore

class LanguageFactory:
    def select_language(language):
        store={
            'python3':LanguageStore.Python3(),
            'php':LanguageStore.PHP(),
            'cpp':LanguageStore.CPP(),
            'python2':LanguageStore.Python2(),
        }
        return store[language]