# Encrypt the message "Sensitive Information" using AES-128 with the following
# key: "0123456789ABCDEF0123456789ABCDEF". Then decrypt the ciphertext
# to verify the original message.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'0123456789ABCDEF0123456789ABCDEF'

# Generate a random 128-bit (16-byte)
iv = get_random_bytes(16)

# Plaintext to encrypt
plaintext = b"Sensitive Information"

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
