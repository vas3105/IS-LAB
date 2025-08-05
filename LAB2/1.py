#  Encrypt the message "Confidential Data" using DES with the following key:
# "A1B2C3D4". Then decrypt the ciphertext to verify the original message.
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'A1B2C3D4'

#Create a DES cipher object in Electronic Codebook (ECB) mode
cipher = DES.new(key, DES.MODE_ECB)

 # Plaintext to encrypt
plaintext = b'Confidential Data'

# Pad the plaintext to be a multiple of the block size (8 bytes for DES)
padded_plaintext = pad(plaintext, DES.block_size)

# Encrypt the padded plaintext
ciphertext = cipher.encrypt(padded_plaintext)
print(f"Ciphertext: ",ciphertext.hex())

# Decrypt the ciphertext
decipher = DES.new(key, DES.MODE_ECB) # Create a new cipher object for decryption
decrypted_padded_text = decipher.decrypt(ciphertext)

# Unpad the decrypted text
decrypted_text = unpad(decrypted_padded_text, DES.block_size)
print(f"Decrypted text: ",decrypted_text)
