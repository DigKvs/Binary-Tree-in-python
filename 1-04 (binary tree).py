class No:
    def __init__(self, valor) :
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def addNo(self, valor):
        if valor>self.valor:
            if self.direita == None:
                self.direita = No(valor)
                print(f"Adicionado {valor} à direita de {self.valor}")
            else:
                self.direita.addNo(valor)
                
        elif valor<self.valor:
            if self.esquerda == None:
                self.esquerda = No(valor)
                print(f"Adicionado {valor} à esquerda de {self.valor}")
            else:
                self.esquerda.addNo(valor)
        
        else :
            self.valor = valor
            print(f"O valor {valor} já existe na árvore. Não foi adicionado novamente.")
            
    def ordemCrescente(self):
        if self.esquerda != None :
            self.esquerda.ordemCrescente()
            
        print(self.valor)
        
        if self.direita != None :
            self.direita.ordemCrescente()
            

raiz = No(int(input("digite sua raiz --> ")))

a = 0
while a == 0:
    op = int(input("digite 1 para continuar, digite 2 para parar --> "))
    if op == 1:
        num = int(input("digite seu numero para colocar na arvore binaria --> "))
        raiz.addNo(num)

    elif op == 2:
        a = 1
    else:
        print("Opção inválida. Tente novamente.")
        


raiz.ordemCrescente()
    
    
    