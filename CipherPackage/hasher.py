from __future__ import annotations
from abc import ABC, abstractmethod

class HashingStrategy(ABC):
    # define operações comuns a todos os algoritmos
    @abstractmethod
    def hasher(self,elements):
        pass
    
class Hasher(HashingStrategy):
    def __init__(self,strategy:Strategy) -> None:
        
        self._strategy= strategy
    
    
    def hasher(self,data):

        elements = list(data)
        result = self._strategy.hasher(elements)
        print(result)
        