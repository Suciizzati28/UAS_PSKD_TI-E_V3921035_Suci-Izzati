from cryptography.fernet import Fernet

# buat kunci
key = Fernet.generate_key() 
# membaca kunci yang tekah dibuat
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

fernet = Fernet(key)

# buka file yang akan di enkripsi
with open('file_csv.csv', 'rb') as file:
    original = file.read()     
# enkripsi 
encrypted = fernet.encrypt(original)
# simpan file yang telah di enkripsi
with open('encrypted.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)



