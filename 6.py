class Pessoa():
    def __init__(self, nome,cargo, salario = 0, aumento = 0.1):
        self.nome = nome
        self.salario = salario 
        self.cargo = cargo
        
    def mostrar(self):
        return(f"{self.nome}, é {self.cargo}, e recebe {self.salario}")
            
    def aumentar(self):
        self.salario *= 0.1
        self.salario *= 11
        
        
        return(f"Você recebeu um aumento, agora você recebe {self.salario} ")
            
     
trabalhador = Pessoa("kleber", "junior", 4000, 0.1)

print(trabalhador.mostrar())

print(trabalhador.aumentar())
