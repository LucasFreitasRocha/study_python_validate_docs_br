from validate_docbr import CPF

class Cpf:
  def __init__(self,document):
    self.lib_cpf = CPF()
    if self.validate_document(document):
      self._document = document
    else:
      raise ValueError("Cpf invalido")
  def getDocument(self):
    return self._document
  def setDocument(self,document):
    self._document = document
  def __str__(self) -> str:
    return self.formatCpf()  
  def formatCpf(self):
    return self.lib_cpf.mask(self._document)
  def validate_document(self,document):
    return self.lib_cpf.validate(document)
