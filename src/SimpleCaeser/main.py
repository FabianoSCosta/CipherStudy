from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

class Encryptor():
    
    def __init__(self,strategy:Strategy) -> None:
        
        self._strategy= strategy

    def encrypt(self,data,key):
        elements = list(data)
        result = self._strategy.Encode(elements,key)
        print(result)
        
class Strategy(ABC):
    # define operações comuns a todos os algoritmos
    @abstractmethod
    def Encode(self,elements,key):
        pass

class SimpleCeaser(Strategy):
    def Encode(self,elements,key):
        
        asciiCharList = list(map(ord,elements))
        asciiCodedList = [np.mod(i+key,127) for i in asciiCharList]
        coded = [chr(i) for i in asciiCodedList]
        return coded
        
if __name__ == "__main__":
    text=input("Enter the text to encrypt")
    key=int(input("Enter the secret key"))
    encryptor = Encryptor(SimpleCeaser())
    encryptor.encrypt(text,key)
    

    
    
    