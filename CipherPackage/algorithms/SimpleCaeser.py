from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

# SimpleCeaser utiliza a tabela ASCII, substituindo pela posição do elemento deslocado pelo inteiro 'key'.
class SimpleCaeser():
    def encode(self,elements,key):
        
        asciiCharList = list(map(ord,elements))
        asciiCodedList = [np.mod(i+key,127) for i in asciiCharList]
        coded = [chr(i) for i in asciiCodedList]
        return coded
        
    def decode(self,elements, key):
        asciiCharList = list(map(ord,elements))
        asciiCodedList = [np.mod(i-key,127) for i in asciiCharList]
        decoded = [chr(i) for i in asciiCodedList]
        return decoded
    

    

    
    
    