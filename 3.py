class Pessoa():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade 
        self.email = email
        
    def mostrar_email(self):
        return self.email
          
    
    def mostrar_nome(self):
        return self.nome
            
    def idades(self, idade2):
        
        if idade2 < 18:
            return ("Menor de idade")
        else:
            return ("maior de idade")
            
     
individuo = Pessoa("joao",15,"joaomimguel@gmail.com")

print(individuo.mostrar_email())

print(individuo.mostrar_nome())

print(individuo.idades(20))
