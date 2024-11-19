class data:
    def __init__(self, dia,mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def mostrar():
        return(self.dia, self.mes, self.ano)
        
        
    def data_correta(self):
        
        
        
        if self.mes > 12 :
            return("data invalida")
        elif self.mes == 2 and self.dia > 29:
            return("Data invalida")
            
        elif self.dia > 31:
            return("Data invalida")
        else:
            return("Data valida")
        


datas = data(10,2,2000)

print(datas.data_correta())
