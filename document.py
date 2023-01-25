from cpf import *
from cnpj import *
class Document():
  
  @staticmethod
  def create_document(document):
      if len(document) == 11:
        return Cpf(document)
      elif len(document) == 14:
        return Cnpj(document)
      else:
        raise ValueError("Invalid document, send a cpf or cnpj")
      
      