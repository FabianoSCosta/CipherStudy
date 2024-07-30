from CipherPackage import *

if __name__ == "__main__":
    text=input("Enter the text to encrypt: ")
    key=input("Enter the secret key: ")
    
    
    encryptor = Encryptor(SimpleCaeser())
    encryptor.encrypt(text,key)