# -*- coding: utf-8 -*-
"""25011540.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12g-4nHzn3fZ1sFQKMPH1OWoqKZSBE7pf
"""

!pip install cryptography

from cryptography.fernet import Fernet

# Generate key

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# message to encrypt

message = b"Ishimwe"

# encrypt
encrypted_message = cipher_suite.encrypt(message)
print("Encrypt message:", encrypted_message)

# descript the message
decrypted_message = cipher_suite.decrypt(encrypted_message)
print("Decrypted_message:", decrypted_message.decode())

#key = Fernet.generate_key()

"""First_Name:

"""