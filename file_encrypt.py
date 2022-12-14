from PyPDF2 import PdfWriter, PdfReader
  
out = PdfWriter()
# buka file pdf
file = PdfReader("file_pdf.pdf")
# identifikasi total halaman file
num = file.numPages
# buat loop untuk setiap halaman
for page in file.pages:
    # tambahkan halaman ke file baru
    out.add_page(page)
    
# buat password
password = "password"
  
# enkripsi file pdf 
out.encrypt(password)
  
# simpan file pdf yang sudah di enkripsi
with open("Encrypted_pdf.pdf", "wb") as f:
    out.write(f)