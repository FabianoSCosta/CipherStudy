from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

class HashXor():
    
    def hasher(self,elements):
        binarycharlist = [format(ord(char), '08b') for char in elements]
        arraystringlist=np.array(binarycharlist)
        
        arraybinarylist = [[int(bit) for bit in binary] for binary in arraystringlist]
         
        
        xorhash = np.bitwise_xor.reduce(arraybinarylist)
        
        return xorhash
        
        