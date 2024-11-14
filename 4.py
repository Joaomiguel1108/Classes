class conta_bancaria():
    def __init__(self, titular, inicial=0):
        self.titular = titular
        self.inicial = inicial    
        
    def mostrar_saldo(self):
        return self.inicial
          
    
    def depositar(self, valor):
        self.inicial += valor
            
    def Sacar(self, valor):
        if valor <= self.inicial:
            self.inicial -= valor
            
        else:
            print("Saldo insuficiente")
        
conta = conta_bancaria("joao", 1000)
print("Saldo inicial", conta.mostrar_saldo() )

conta.depositar(200)
print("Saldo apos o saque", conta.mostrar_saldo())

conta.Sacar(200)
print("Saldo após saque:", conta.mostrar_saldo())

conta.Sacar(500)
            
