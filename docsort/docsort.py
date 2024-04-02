'''
Created on 02.04.2024

@author: neumann
'''

class DocSort(object):

    def __init__(self, scanPath, docPath):
        self.scanPath = scanPath
        self.docPath  = docPath
    
    def getDocs(self):
        return 0

    def getDoc(self, idx):
        return idx

    def convertDoc(self, idx):
        return 0
    

if __name__ == "__main__":
    docs = DocSort("scans", "docs" )



