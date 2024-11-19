class retangulo:
    def __init__(self, altura,largura):
        self.altura = altura
        self.largura = largura
        
    def area(self):
        
        return(self.altura*self.largura)
        
    def perimetro(self):
        
        return (self.altura*2 + self.largura*2)

calculo = retangulo(10,20)



print(calculo.area())
print(calculo.perimetro())
