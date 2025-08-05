#  Encrypt the message "I am learning information security" using each of the
# following ciphers. Ignore the space between words. Decrypt the message to
# get the original plaintext:
# a) Additive cipher with key = 20
# b) Multiplicative cipher with key = 15
# c) Affine cipher with key = (15, 20)
def encrypt_text(plaintext,k):
    ans=""

    for i in range(len(plaintext)):
        ch=plaintext[i]
        if ch==" ":
            continue
        elif (ch.isupper()):
            ans+=chr((ord(ch)+k-65)%26+65)
        else:
            ans+=chr((ord(ch)+k-97)%26+97)
    return ans

def decrypt_text(ciphertext,k):
    ans = ""
    for ch in ciphertext:
        if ch == " ":
            ans += " "  # Keep spaces in the result
        elif ch.isupper():
            ans += chr((ord(ch) - k - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) - k - 97) % 26 + 97)
    return ans

def multi_encrypt(plaintext,k):
    ans=""
    for char in plaintext:
        if char.isalpha():
           num = ord(char.lower()) -ord('a')
           encrypted_num=(num*k)%26
           ans+=chr(encrypted_num+ord('a'))
        else:
            ans+=char
    return ans

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def multi_decrypt(ciphertext,k):
    ans = ""
    if gcd(k, 26) != 1:
        raise ValueError(f"The key {k} is not invertible modulo 26.")
    inverse_key = pow(k,-1,26)
    for char in ciphertext:
        if char.isalpha():
            is_upper=char.isupper()
            num = ord(char.lower()) -ord('a')
            decrypted_num=(num*inverse_key)%26
            ans+=chr(decrypted_num+ord('a'))
            if is_upper:
                decrypted_char=decrypted_num.upper()
                ans+= decrypted_char
        else:
            ans+=char
    return ans

def affine_encrypt(plaintext,a,b):
    ans=""
    for i in range(len(plaintext)):
        ch=plaintext[i]
        if ch==" ":
            continue
        elif (ch.isupper()):
            ans+=chr((ord(ch)*a+b-65)%26+65)
        else:
            ans+=chr((ord(ch)*a+b-97)%26+97)
    return ans

def affine_decrypt(ciphertext, a, b):
    ans = ""
    if gcd(a, 26) != 1:
        raise ValueError(f"The key {a} is not invertible modulo 26.")
    inverse_key = pow(a, -1, 26)
    for ch in ciphertext:
        if ch == " ":
            ans += " "
        elif ch.isupper():
            # Correctly apply modulus after subtracting 'b' to avoid negative results
            decrypted_char = (inverse_key * (ord(ch) - 65 - b)) % 26
            decrypted_char = (decrypted_char + 26+10) % 26  # Ensure non-negative results
            ans += chr(decrypted_char + 65)
        else:
            decrypted_char = (inverse_key * (ord(ch) - 97 - b)) % 26
            decrypted_char = (decrypted_char + 26+10) % 26  # Ensure non-negative results
            ans += chr(decrypted_char + 97)

    return ans


print("enter the plaintext")
plaintext=input()
print("Plain text: "+plaintext)
print("Additive cipher")
ciphertext=encrypt_text(plaintext,20)
print("Cipher text is : "+ciphertext)
print("Plain text after decryption is : "+decrypt_text(ciphertext,20))
print("Multiplicative cipher")
decipher_text=multi_encrypt(plaintext,15)
print("after encryption is : "+decipher_text)
print("after decryption is : "+multi_decrypt(decipher_text,15))
print("Affine cipher")
cipher_text=affine_encrypt(plaintext,15,20)
print("Cipher text after encryption is : "+cipher_text)
print("Cipher text after decryption is : "+affine_decrypt(cipher_text,15,20))
