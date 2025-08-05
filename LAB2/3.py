# Compare the encryption and decryption times for DES and AES-256 for the
# message "Performance Testing of Encryption Algorithms". Use a standard
# implementation and report your findings.
import timeit
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

plaintext = b"Performance Testing of Encryption Algorithms"

des_key = get_random_bytes(8)
des_iv = get_random_bytes(8)

aes_key = get_random_bytes(32)
aes_iv = get_random_bytes(16)


def des_encrypt_decrypt():
    # Create DES cipher in CBC mode
    cipher = DES.new(des_key, DES.MODE_CBC, des_iv)
    padded = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded)

    decipher = DES.new(des_key, DES.MODE_CBC, des_iv)
    decrypted_padded = decipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, DES.block_size)
    assert decrypted == plaintext


def aes_encrypt_decrypt():
    # Create AES cipher in CBC mode
    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    padded = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded)

    decipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    decrypted_padded = decipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, AES.block_size)
    assert decrypted == plaintext


# Measure times
des_time = timeit.timeit(des_encrypt_decrypt, number=1)
aes_time = timeit.timeit(aes_encrypt_decrypt, number=1)

print(f"DES (CBC) encryption+decryption time: {des_time:.6f} seconds")
print(f"AES-256 (CBC)encryption+decryption time: {aes_time:.6f} seconds")
