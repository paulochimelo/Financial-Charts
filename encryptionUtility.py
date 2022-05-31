from cryptography.fernet import Fernet
from sys import argv

key = Fernet.generate_key()
f = Fernet(key)

stringArgument = argv[1]
encryptedValue = f.encrypt(bytes(stringArgument, encoding='utf-8'))

print('Output key:')
print(key.decode('utf-8'))
print('Output value:')
print(encryptedValue.decode('utf-8'))