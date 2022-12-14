from cryptography.fernet import Fernet

# Dekripsi

# Buka kunci yang sudah dibuat
key = open('filekey.key', 'rb').read()
fernet = Fernet(key)

# buka file yang telah dienkripsi
with open('encrypted.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# dekripsi file yang telah dienkripsi
decrypted = fernet.decrypt(encrypted)

# buat file baru yang sudah terdekripsi
with open('decrypted.csv', 'wb') as dec_file:
	dec_file.write(decrypted)