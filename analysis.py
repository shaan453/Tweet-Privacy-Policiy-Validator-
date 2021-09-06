from data_loader import *

class analysis:
    def checking(self,sentence):
        dl = data_loader()
        blacklist = dl.load()
        for i in range(len(blacklist)):
            if blacklist[i] in sentence:
                return True
        return False
        
