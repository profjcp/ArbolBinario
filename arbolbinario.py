from Node import Node

class arbolB:
    def __init__(self):
        self.raiz=Node()
        self.raiz=None
   
    def insertar(self,ele):
        nuevo=Node()
        nuevo.setelemento(ele)
        
        if self.raiz==None:
            self.raiz=nuevo 
        else:
            aux=self.raiz
            
            while aux!=None:
                padre=aux
                if(ele<aux.getElemento()):
                    aux=aux.gethijoizq()
                else:
                    aux=aux.gethijoder()
            if padre.getElemento()>nuevo.getElemento():
                padre.Hizq=nuevo 
                '''padre.gethijoizq().sethijoizq(nuevo)'''
            else:
                padre.Hder=nuevo
                '''padre.gethijoder().sethijoder(nuevo)'''             

    def recorrer(self,n):
        if(n!=None):
            self.recorrer(n.gethijoizq())
            print(n.getElemento())
            self.recorrer(n.gethijoder())  
         
    
def main():
   a=arbolB()
   a.insertar(15)
   a.insertar(6)
   a.insertar(20)
   a.insertar(3)
   a.insertar(9)
   a.insertar(18)
   a.insertar(24)
   a.insertar(1)
   a.insertar(4)
   a.insertar(7)
   a.insertar(12)
   a.insertar(17)
   a.recorrer(a.raiz)
if __name__=='__main__':
   main()
