from validate_docbr import CPF

class Cpf:
  def __init__(self,document):
    print("inciando classe cpf com documento")
    self.lib_cpf = CPF()
    if self.validateDocument(document):
      self._document = document
    else:
      raise ValueError("Cpf com tamanho invalido")
  def getDocument(self):
    return self._document
  def setDocument(self,document):
    self._document = document
  def __str__(self) -> str:
    return self.formatCpf()  
  def formatCpf(self):
    return self.lib_cpf.mask(self._document)
  def validateDocument(self,document):
    return self.lib_cpf.validate(document)
