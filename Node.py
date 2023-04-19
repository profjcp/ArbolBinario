'''
title: class nodo
autor: rafael lopez gutierrez
created:2023-04-11
version: 1.0
'''

class Node:
    '''metodo que inicializa la clase nodo'''
    '''self.__elemento  significa q es un atributo privado'''
    '''def __getelemento  igul en fucniones si se pone con guion bajo se hace metodo privado'''
    def __init__(self):
        self.Hizq=None
        self.Hder=None
        self.elemento=0   
    '''@property'''
    def getElemento(self):   
        p=self.elemento
        return (p)    
    def gethijoizq(self):
        p=self.Hizq   
        return (p)
    def gethijoder(self):
        p=self.Hder   
        return (p)   
    
    
    '''@setelemento.setter'''
    def setelemento(self,x):
        self.elemento = x
    def sethijoizq(self,x):
        self.Hizq=x
    def sethijoder(self,x):
        self.Hder=x 
