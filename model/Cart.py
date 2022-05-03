'''
Created on 03-05-2022

@author: alvar
'''

class Cart():
    def __init__(self,identifier,path):
        self.__id=identifier
        self.__imagePath=path
        
    def getId(self):
        return self.__id
    
    def getPath(self):
        return self.__imagePath