# Encrypt the message "Classified Text" using Triple DES with the key
# "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF". Then
# decrypt the ciphertext to verify the original message.
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

iv=get_random_bytes(8)
full_key=b"1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"
# Trim to first 24 bytes for DES3 key
key=full_key[:24]

plaintext=b"Classified Text"
cipher = DES3.new(key, DES3.MODE_CBC,iv)
#encrypt
ciphertext = cipher.encrypt(pad(plaintext,DES3.block_size))
print("Cipher text: ",ciphertext.hex())
#decrypt
decipher = DES3.new(key, DES3.MODE_CBC,iv)
decrypted = unpad(decipher.decrypt(ciphertext),DES3.block_size)
print("Decrypted text: ",decrypted)




