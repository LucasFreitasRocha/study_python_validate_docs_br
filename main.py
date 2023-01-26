from phones import PhonesBr 
from document import Document
document_cpf="73056261040"
document_cnpj="22338768000102"
print("CPF:  " , Document.create_document(document_cpf))
print("CNPJ: ", Document.create_document(document_cnpj))
print("Celular: ", PhonesBr("5522997318077"))

