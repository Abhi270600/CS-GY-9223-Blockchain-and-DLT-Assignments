from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random key and initialization vector (IV)
key = os.urandom(32)  # 256-bit key for AES-256
iv = os.urandom(16)   # 128-bit IV

# Create a cipher object
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

# Encrypt
encryptor = cipher.encryptor()
plaintext = b"Hello, this is a secret message!"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Decrypt
decryptor = cipher.decryptor()
decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

print(f"Original: {plaintext}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {decrypted_text}")