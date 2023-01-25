from document import Document

document_cpf= "73056261040"
document_cnpj="22338768000102"
print(Document.create_document(document_cpf))
print(Document.create_document(document_cnpj))

