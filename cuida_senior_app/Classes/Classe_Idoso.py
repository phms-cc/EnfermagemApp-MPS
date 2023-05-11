# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:40:53 2023

@author: filip
"""

class Idoso():
    def __init__(self,i,atributos,endereco,comorbidades):
        self.id = i
        self.nome = atributos[0]
        self.idade = atributos[1]
        self.peso = atributos[2]
        self.altura = atributos[3]
        self.endereco = endereco
        self.comorbidades = comorbidades
        #tornar enum?
    
    def getID(self):
        return self.id
    
    def compareID(self, i):
        return (self.id == i)
    
    def getNome(self):
        return self.nome
    
    def setNome(self,nome):
        self.nome = nome
    
    def getIdade (self):
        return self.idade
    
    def setIdade(self,idade):
        self.idade = idade
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self,peso):
        self.peso = peso
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self,altura):
        self.altura = altura
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self,endereco):
        self.endereco = endereco
    
    
    def getComorbidades(self):
        return self.comorbidades
    
    def addComorbidade(self,comorbidade):
        self.comorbidades.append(comorbidade)
    
    def temComorbidade(self,comorbidade):
        return (comorbidade in self.comorbidades)
    
    def nComorbidades(self):
       return len(self.comorbidades)
    
    def removeComorbidade(self,comorbidade):
        if(isinstance(comorbidade, int)):
            if(comorbidade<self.nComorbidades()):
                del self.comorbidades[comorbidade]
            #poderia fazer um else com excecao
        elif (isinstance(comorbidade, str)):
            if(self.temComorbidade(comorbidade)):
                self.comorbidades.remove(comorbidade)
            #poderia fazer um else com excecao
        
class IdosoControle:
    def __init__(self):
        self.idosos = []
        self.id_contagem = 0
        #basicamente, essa variavel vai servir pra dar um id diferente para cada idoso
        
    
    def cria_idoso(self,atributos,endereco,comorbidades):
        idoso = Idoso(self.id_contagem,atributos,endereco,comorbidades)
        self.id_contagem+=1
        return idoso
    
    def add_idoso(self,idoso):
        self.idosos.append(idoso)
        
    def cria_add_idoso(self,atributos,endereco,comorbidades):
        self.add_idoso(self.cria_idoso(atributos,endereco,comorbidades))
    
    def search_idoso_id(self,i):
        for idoso in self.idosos:
            if (i == idoso.getID()):
                return idoso

    def list_comorbidades(self,idoso):
        comorbidades = idoso.getComorbidades()
        for comorbidade in comorbidades:
            print(comorbidade, end = " ")

    def list_idoso(self,idoso):
        print("Nome: " + idoso.getNome() + " idade:" + str(idoso.getIdade()),end = "")
        print(" peso:" + str(idoso.getPeso())+ " altura:" + str(idoso.getAltura()))
        
    def list_idosos(self):
        for idoso in self.idosos:
            self.list_idoso(idoso)
            
    def delete_idoso(self,i):
        for idoso in self.idosos():
            if (i==idoso.getID()):
                self.idosos.remove(idoso)
                break
            
    def idoso_getNome(self,i):
        idoso =self.search_idoso_id(self,i)
        idoso.getNome()

    def idoso_setNome(self,i,nome):
        idoso =self.search_idoso_id(self,i)
        idoso.setNome(nome)

    def idoso_getIdade(self,i):
        idoso =self.search_idoso_id(self,i)
        idoso.getIdade()

    def idoso_setIdade(self,i,idade):
        idoso =self.search_idoso_id(self,i)
        idoso.setIdade(idade)

    def idoso_getAltura(self,i):
        idoso =self.search_idoso_id(self,i)
        idoso.getAltura()

    def idoso_setAltura(self,i,altura):
        idoso =self.search_idoso_id(self,i)
        idoso.setAltura(altura)

    def idoso_getPeso(self,i):
        idoso =self.search_idoso_id(self,i)
        idoso.getPeso()

    def idoso_setPeso(self,i,peso):
        idoso =self.search_idoso_id(self,i)
        idoso.setPeso(peso)
    
    def idoso_getEndereco(self,i):
        idoso =self.search_idoso_id(self,i)
        idoso.getEndereco()


    def idoso_setEndereco(self,i,endereco):
        idoso =self.search_idoso_id(self,i)
        idoso.setPeso(endereco)

    
class IdosoForm:
    def __init__(self):
        pass