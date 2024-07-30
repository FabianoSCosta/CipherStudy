from __future__ import annotations
from abc import ABC, abstractmethod


class EncryptorStrategy(ABC):
    # define operações comuns a todos os algoritmos
    @abstractmethod
    def encrypt(self,data,key):
        pass
    
    @abstractmethod
    def decrypt(self,data,key):
        pass

class Encryptor(EncryptorStrategy):
    
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
        result = self._strategy.encrypt(elements,key)
        print(result)
        
    def decrypt(self,data,key):
        key = self._convert_key(key)
        elements = list(data)
        result = self._strategy.decrypt(elements,key)
        print(result)
        
    