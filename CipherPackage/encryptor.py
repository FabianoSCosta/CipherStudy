from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):
    # define operações comuns a todos os algoritmos
    @abstractmethod
    def encode(self,elements,key):
        pass
    
    @abstractmethod
    def decode(self,elements,key):
        pass

class Encryptor():
    
    def __init__(self,strategy:Strategy) -> None:
        
        self._strategy= strategy
        
    def _convert_key(self, key):
        if key.isdigit():
            return int(key)
        else:
            return ord(key)

    def encrypt(self,data,key):
        key = self._convert_key(key)
        elements = list(data)
        result = self._strategy.encode(elements,key)
        print(result)
        
    def decrypt(self,data,key):
        key = self._convert_key(key)
        elements = list(data)
        result = self._strategy.decode(elements,key)
        print(result)
        
    