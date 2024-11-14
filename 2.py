class livros():
    def __init__(self, nome, ano, autor):
        self.nome = nome
        self.ano = ano 
        self.autor = autor
        
    def mostrar_autor(self):
        return self.autor
          
    
    def mostrar_nome(self):
        return self.nome
            
    def ano(self,ano2):
        print(ano)
        if ano2 > 2000:
            return("Foi publicado depois de 2000")
        else:
            return("Antes de 2000")
            
     
livro = livros("Senhor dos anéis", 1954, "J. R. R. Tolkien")

print(livro.mostrar_nome())

print(livro.mostrar_autor())

print(livro.ano(1954))


 
            





    
