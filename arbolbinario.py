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
            elif padre.getElemento()<nuevo.getElemento():
                padre.Hder=nuevo
                '''padre.gethijoder().sethijoder(nuevo)'''  
            else:
                print("el dato "+ repr(ele)+" ya se encuentra en el arbol")  
                             

    def preOrden(self,n):
        if(n!=None):
            print(n.getElemento())
            self.preOrden(n.gethijoizq())
            self.preOrden(n.gethijoder())  
    def inOrden(self,n):
        if(n!=None):
            self.inOrden(n.gethijoizq())
            print(n.getElemento())
            self.inOrden(n.gethijoder())     
    def posOrden(self,n):
        if(n!=None):
            self.posOrden(n.gethijoizq())
            self.posOrden(n.gethijoder())   
            print(n.getElemento()) 
    '''
    def eliminarRecursivo(self,n,ele):
        if(n!=None):
            if n.getElemento()<ele:
                self.eliminarRecursivo(n.gethijoizq())
                self.eliminarRecursivo(n.gethijoder())
        

    def eliminar(self,ele):
        if ele< self.raiz.getElemento():
            self.eliminarRecursivo(self.raiz.gethijoizq(),ele)
        
        else: 
            self.eliminarRecursivo(self.raiz.gethijoder(),ele)    
    '''  
    
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
   a.insertar(17)
   a.insertar(17)
   a.posOrden(a.raiz)
if __name__=='__main__':
   main()  