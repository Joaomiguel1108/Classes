class aluno:
    def __init__(self, nome,matricula, nota=  0, notar = 0, notas =0):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.notar = notar
        self.notas = notas
        
    def media(self):
        
        conta = (self.nota+self.notar+self.notas)/3
        
        if conta > 6:
            return(f"{self.nome}, Você foi aprovado!")
            
        else:
            return(f"{self.nome} Você foi reprovado")
            
aluno1 = aluno("joão",1100554579,1,6,3)



print(aluno1.media())
