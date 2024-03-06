import base64
import os

Option = int(input("[1] Decrypt [2] Encrypt >> "))

if Option == 1:
    EncryptedMessage = input("Message to Decrypt? ")

    EncryptedMessage_bytes = EncryptedMessage.encode("ascii") 
    base64_bytes = base64.b64decode(EncryptedMessage_bytes) 
    base64_string = base64_bytes.decode("ascii") 

    print(base64_string)

if Option == 2:
    EncryptedMessage = input("Message to Encrypt? ")

    EncryptedMessage_bytes = EncryptedMessage.encode("ascii")
    base64_bytes = base64.b64encode(EncryptedMessage_bytes) 
    base64_string = base64_bytes.decode("ascii")  

    print(base64_string)
