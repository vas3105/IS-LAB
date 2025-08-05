# Encrypt the message "Top Secret Data" using AES-192 with the key
# "FEDCBA9876543210FEDCBA9876543210". Show all the steps involved in
# the encryption process (key expansion, initial round, main rounds, final round).
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

full_key = b'FEDCBA9876543210FEDCBA9876543210'
key=full_key[:24]

# Generate a random 128-bit (16-byte)
iv = get_random_bytes(16)

# Plaintext to encrypt
plaintext = b"Top Secret Data"

# Create AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the padded plaintext
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Decrypt the ciphertext
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print(f"Original Plaintext: ",plaintext)
print(f"Ciphertext: ",ciphertext.hex())
print(f"Decrypted Plaintext: ",decrypted_plaintext)
