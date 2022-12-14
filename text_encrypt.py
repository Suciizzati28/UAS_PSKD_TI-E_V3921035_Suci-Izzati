from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Masukkan file yang akan di enkripsi
file_to_encrypt = open('file_txt.txt', 'rb')
data = file_to_encrypt.readlines()

# mendifiniskan lines pada file  kemudian men encode text nya
txt = str(data[11])
txt_binary = txt.encode()

# buat public key
keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()

# Enkripsi
chiper = PKCS1_OAEP.new(pubKey)
encrypted = chiper.encrypt(txt_binary)
binnary = binascii.hexlify(encrypted)

# File tidak akan di print pada terminal
# print("Encrypted: ", binascii.hexlify(encrypted))

# Dekripsi
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plaintext = decrypted.decode()
print("Decrypted: ", plaintext)


# Buat file baru yang sudah ter enkripsi
with open('encrypted_file.txt', 'wb') as file_out:
    file_out.write(binnary)

# with open('decrypted_file.txt', 'wb') as file:
#     file.write(plaintext)